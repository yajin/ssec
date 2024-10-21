#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

long int id = 1;

void get_shell()
{
    if(id == 1234)
       system("/bin/sh");
}

void echo()
{
    printf("You can type exactly 256 charecters ...\n");
    char buffer[256];
    read(STDIN_FILENO, buffer, 256);
    printf(buffer);
    puts("done");
    return;
}
int main(int argc, char* argv[])
{
    echo();
    return 0;
}
