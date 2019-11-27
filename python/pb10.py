'''
Task: Consider a list (list = []). You can perform the following commands:
- insert i e: Insert integer e at position i.
- print: Print the list.
- remove e: Delete the first occurrence of integer e.
- append e: Insert integer e at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.
--------------------------------------------------------------------------------------------------
Sample Input:
              12
              insert 0 5
              insert 1 10
              insert 0 6
              print
              remove 6
              append 9
              append 1
              sort
              print
              pop
              reverse
              print
Sample Output:
              [6, 5, 10]
              [1, 5, 9, 10]
              [9, 5, 1]
'''
if __name__ == '__main__':
    N = int(input())
    # Scan the inputs in a 2D list
    l = []
    for i in range(N):
        l.append(input().split())

    # Prepare the output
    out = []
    for i in range(N):
    	inst = l[i][0]
    	if inst == 'insert':
    		out.insert(int(l[i][1]),int(l[i][2]))
    	elif inst == 'print':
    		print(out)
    	elif inst == 'remove':
    		out.remove(int(l[i][1]))
    	elif inst == 'append':
    		out.append(int(l[i][1]))
    	elif inst == 'sort':
    		out.sort()
    	elif inst == 'pop':
    		out.pop(-1)
    	elif inst == 'reverse':
    		out.reverse()