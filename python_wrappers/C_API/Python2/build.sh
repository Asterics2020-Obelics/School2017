gcc -c  hellomodule.c `python2.7-config --cflags` `python2.7-config --ldflags` -o hellomodule.o
gcc -pthread -shared hellomodule.o -o hello.so
