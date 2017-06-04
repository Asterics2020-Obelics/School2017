'''
Example vectorize usage.
'''

from __future__ import print_function
import numpy as np
from numba import *
from timeit import default_timer as time
import math
import sys

if sys.version_info[0] == 2:
    from itertools import izip as zip

def generate_input(n, dtype):
    A = np.array(np.random.sample(int(n)), dtype=dtype)
    B = np.array(np.random.sample(int(n)) + 10, dtype=dtype)
    C = np.array(np.random.sample(int(n)), dtype=dtype)
    return A, B, C

def check_answer(ans, A, B, C):
    for d, a, b, c in zip(ans, A, B, C):
        gold = discriminant(a, b, c)
        assert np.allclose(d, gold), (d, gold)

def discriminant(a, b, c):
    '''a ufunc kernel to compute the discriminant of quadratic equation
    '''
    return math.sqrt(b ** 2 - 4 * a * c)


def main():

    N = 1e+9 // 2
    print('Data size', N)

    targets = ['cpu', 'parallel']
    
    # run just one target if is specified in the argument
    for t in targets:
        if t in sys.argv[1:]:
            targets = [t]
            break

    for target in targets:
        print('== Target', target)
        vect_discriminant = vectorize([f4(f4, f4, f4), f8(f8, f8, f8)],
                                    target=target)(discriminant)

        A, B, C = generate_input(N, dtype=np.float32)
        D = np.empty(A.shape, dtype=A.dtype)

        ts = time()
        D = vect_discriminant(A, B, C)
        te = time()

        total_time = (te - ts)

        print('Execution time %.4f' % total_time)
        print('Throughput %.4f' % (N / total_time))



        if '-verify' in sys.argv[1:]:
            check_answer(D, A, B, C)


if __name__ == '__main__':
    main()
