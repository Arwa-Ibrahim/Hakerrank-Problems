#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /*
     * to take single character: scanf("%c", &ch) 
     * Note: to print it you needn't to put the & (pass by ref)
     * to take a line as input:  scanf("%[^\n]%*c", s) where:
     * s is defined as char s[max_number_of_characters]
     * [] is the scanset character
     * ^\n stands for taking input until a newline isn't encountered
     * %*c, it reads the newline character and here, the used * indicates that this newline character is discarded
     *************************************************************************************************************
     * sample input:
     *              C
     *              Language
     *              Welcome To C!!
     * sample output:
     *              C
     *              Language
     *              Welcome To C!!
    */


    /* Note: After inputting the character and the string,
     * inputting the sentence by the above mentioned statement won't work.
     * This is because, at the end of each line, a new line character (\n) is present.
     * So, the statement: scanf("%[^\n]%*c", s); will not work
     * because the last statement will read a newline character from the previous line.
     * This can be handled in a variety of ways and one of them being: scanf("\n"); before the last statement.
    */

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char ch;
    char s[100];
    char sen[100];

    scanf("%c", &ch);
    scanf("\n");
    scanf("%[^\n]%*c", &s);
    scanf("\n");
    scanf("%[^\n]%*c", &sen);

    printf("%c\n%s\n%s\n", ch, s, sen);

    return 0;
}