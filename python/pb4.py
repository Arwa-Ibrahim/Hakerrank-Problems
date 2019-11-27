'''
Task: Read a non-negative integer and print squred of integres less than it.
---------------------------------------------------------------------------
Sample Input: 5
Sample Output: 
			  0
			  1
			  4
			  9
			  16
'''

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)