'''
Task: Given an integer, , print the following values for each integer  from  to :
Decimal, Octal, Hexadecimal (capitalized) and Binary
The four values must be printed on a single line in the order specified above
for each i from 1 to n. Each value should be space-padded to match the width of the binary value of n.
--------------------------------------------------------------------------
Sample Input:
              2
Sample Output:
               1  1  1  1
               2  2  2 10
'''

def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
    	width = len("{0:b}".format(n))
    	print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
    	#oc = oct(i).lstrip("0o")
    	#he = hex(i).lstrip("0x")
    	#bi = bin(i).lstrip("0b")
    	#print(i, end = " ")
    	#print(str(oc).rjust(width, " "), end = " ")
    	#print(str(he).rjust(width, " "), end = " ")
    	#print(str(bi).rjust(width, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)