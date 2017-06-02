from __future__ import print_function

import math
from timeit import default_timer as time

import numpy as np

from numba import cuda, float32


bpg = 50
tpb = 32
n = bpg * tpb


@cuda.jit
def cu_square_matrix_mul(A, B, C):
    sA = cuda.shared.array(shape=(tpb, tpb), dtype=float32)
    sB = cuda.shared.array(shape=(tpb, tpb), dtype=float32)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bx = cuda.blockIdx.x
    by = cuda.blockIdx.y
    bw = cuda.blockDim.x
    bh = cuda.blockDim.y

    x = tx + bx * bw
    y = ty + by * bh

    acc = 0.
    for i in range(bpg):
        if x < n and y < n:
            sA[ty, tx] = A[y, tx + i * tpb]
            sB[ty, tx] = B[ty + i * tpb, x]

        cuda.syncthreads()

        if x < n and y < n:
            for j in range(tpb):
                acc += sA[ty, j] * sB[j, tx]

        cuda.syncthreads()

    if x < n and y < n:
        C[y, x] = acc

A = np.array(np.random.random((n, n)), dtype=np.float32)
B = np.array(np.random.random((n, n)), dtype=np.float32)
C = np.empty_like(A)

print("N = %d x %d" % (n, n))

s = time()
stream = cuda.stream()
with stream.auto_synchronize():
    dA = cuda.to_device(A, stream)
    dB = cuda.to_device(B, stream)
    dC = cuda.to_device(C, stream)
    for x in range(0,10):
        cu_square_matrix_mul[(bpg, bpg), (tpb, tpb), stream](dA, dB, dC)
        dC.to_host(stream)

e = time()
tcuda = e - s

# Host compute
Amat = np.matrix(A)
Bmat = np.matrix(B)

s = time()
for x in range(0,10) :
    Cans = Amat * Bmat
e = time()
tcpu = e - s

print('cpu:  %f' % tcpu)
print('cuda: %f' % tcuda)
print('cuda speedup: %.2fx' % (tcpu / tcuda))

# Check result
assert np.allclose(C, Cans)

