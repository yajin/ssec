#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define LENGTH 32

void hear(void)
{
    char str[LENGTH];
    puts("[*] Please input some data:");
    read(STDIN_FILENO, str, LENGTH+0x48);
    return;
}

int main(int argc, char **argv)
{
    puts("[*] Ret2libc");
    hear();
    return 0;
}
