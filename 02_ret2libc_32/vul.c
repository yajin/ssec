#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int vul()
{
    char buffer[32] = {0};
    register void *ebp asm ("ebp");
    //printf("ebp: %p \n", ebp);
    //printf("buffer: %p \n", buffer);
    //printf("ebp - buf : %d \n", (unsigned int)ebp - (unsigned int)buffer);
    gets(buffer); 
    return 1;
}

int main(int argc, char **argv)
{
    printf("ret2libc start \n");
    char *shell = (char *) getenv("MYSHELL");
    if (shell) {
        printf("address %p \n", shell);
    }
    vul(); 
    printf("ret2libc end \n");
    return(0);
}



