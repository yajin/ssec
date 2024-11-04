#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char *a, *b, *c;
	char *protect, *recatch;
	
	a = (char *)malloc(0x8);
	b = (char *)malloc(0x18);
	c = (char *)malloc(0x20);
	protect = malloc(0x100);
        /* debug checkpoint - 0 */

	free(a);
	free(b);
	free(c);
	/* debug checkpoint - 1 */

	recatch = malloc(0x10);
	/* debug checkpoint - 2 */

	free(protect);
	free(recatch);
	/* debug checkpoint - 3 */

	exit(0);
}
