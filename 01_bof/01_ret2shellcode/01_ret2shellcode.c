#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define LENGTH 32 

void welcome(void)
{
	char name[0x20];
	char str[LENGTH];
	puts("[*] Tell me your name:");
	read(STDIN_FILENO, name, 0x20);
	printf("[*] Hi, %s. Your name is stored at: 0x%12llX\n", name, (unsigned long long )name);
	puts("[*] Now, give me something to overflow me!");
	gets(str);
	return;
}

int main(void)
{
	printf("[*] Welcome to ret2shellcode.\n");
	welcome();
	return 0;
}

