'''
Task: ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

- It must contain at least 2 uppercase English alphabet characters.
- It must contain at least 3 digits (0 - 9).
- It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
- No character should repeat.
- There must be exactly 10 characters in a valid UID.

------------------------------------------------------------------------------------------------
Sample Input:
                2
                B1CD102354
                B1CDEF2354
Sample Output:
                Invalid
                Valid

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import Counter

def is_valid(ID):
    upper_count = sum(1 for c in ID if c.isupper())
    digits = sum(c.isdigit() for c in ID)
    length = len(ID)
    pattern = re.compile("[A-Za-z0-9]+")
    # Check if ID only contain alphanumeric characters
    if pattern.fullmatch(ID) is not None:
        only_char = True
    else:
        only_char = False
    # Check if there are duplicated charachters
    # Counter function return dictionary with keys is the char and value is the number of repition
    dict = Counter(ID) 
    no_dup = True 
    if len(dict) < len(ID):
        no_dup = False
    # Check if all the conditions are met
    # print (upper_count, digits, length, only_char, no_dup)
    if (upper_count >= 2) and (digits >= 3) and (length == 10) and only_char and no_dup:
            return 'Valid'
    else:
        return 'Invalid'
###############################################  Main Function  ###############################################

n = int(input())
id = []
for i in range(n):
    id.append(input())

for i in range(n):
    print(is_valid(id[i]))