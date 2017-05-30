swig -python modarray.i
gcc -fPIC -c array_sum.c modarray_wrap.c -I/home/jacquem/anaconda3/include/python3.5m
gcc -shared array_sum.o modarray_wrap.o -o _modarray.so

