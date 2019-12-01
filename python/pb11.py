'''
Task: Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
--------------------------------------------------------------------------
Sample Input:
              5
              2 3 6 6 5
Sample Output:
              5
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # convert the array to set to remove the duplicates then convert it back to list
    arr = list(set(arr))
    # sort the array after removing dup. in descending order
    arr.sort(reverse = True)
    print(arr[1])