#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    /*
    * %d (integer), %c (character), %s (string), %f (float)respectively.
    * to print float rounded to n decimal digits no. we can use %.nf where n is the no of digits.
    **********************************************************
    * sample input:
    *               10 4
    *               4.0 2.0
    * sample output:
    *               14 6
    *               6.0 2.0
    */

	int a,b;
    float c,d;

    scanf("%d %d\n", &a, &b);
    scanf("%f %f\n", &c, &d);

    printf("%d %d\n", a+b, a-b);
    printf("%.1f %.1f", c+d, c-d);

    return 0;
}