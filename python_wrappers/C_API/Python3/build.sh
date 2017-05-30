gcc -fPIC -c  hellomodule.c `python3.5-config --cflags` `python3.5-config --ldflags` -o hellomodule.o
gcc -pthread -shared hellomodule.o -o hello.so
