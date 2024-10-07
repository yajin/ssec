#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define LENGTH 32

int func(int a, int b, int c, int d, int e, int f, int g, int h, int i)
{
    int x = a + b + c + d + e + f + g + h + i;
    return x;
}

int main(int argc, char **argv)
{
    puts("[*] x86-64 ");
    int x = func(1, 2, 3, 4, 5 , 6 , 7, 8, 9);
    printf ("x %d \n", x);
    return 0;
}
