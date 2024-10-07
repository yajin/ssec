#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int vul()
{
    char buffer[32] = {0};
    gets(buffer); 
    return 1;
}

int main(int argc, char **argv)
{
    printf("ret2libc start\n");
    vul(); 
    printf("ret2libc end \n");
    return(0);
}



