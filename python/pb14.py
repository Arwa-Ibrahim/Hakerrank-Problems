'''
Task: Given an integer n, and n space-separated integers as input,
create a tuple t, of those  integers. Then compute and print the result of hash(t).
--------------------------------------------------------------------------
Sample Input:
              2
              1 2
Sample Output:
              3713081631934410656
'''

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # hash() returns the hash value of the object if it has one.
    # Hash values are integers.
    # They are used to quickly compare dictionary keys during a dictionary lookup.
    # Numeric values that compare equal have the same hash value even if they are of different types.
    t = tuple(integer_list)
    print(hash(t))