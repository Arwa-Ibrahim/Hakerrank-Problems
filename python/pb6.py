'''
Task: You are given the year, and you have to write a function to check if the year is leap or not.
--------------------------------------------------------
Sample Input: 1990
Sample Output: False

'''

def is_leap(year):
    leap = False
    # Write your logic here
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = False
            if year%400 == 0:
                leap = True   
    return leap

year = int(input())
print(is_leap(year))