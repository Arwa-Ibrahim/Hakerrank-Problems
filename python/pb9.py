'''
Task: Given the names and grades for each student in a Physics class of n students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.
--------------------------------------------------------------------------
Sample Input:
              5
              Harry
              37.21
              Berry
              37.21
              Tina
              37.2
              Akriti
              41
              Harsh
              39
Sample Output:
              Berry
              Harry
'''
from collections import Counter
# function to return the second element of the 
# two elements passed as the parameter 
def sortSecond(val): 
    return val[1] 

if __name__ == '__main__':
    # Create 2 lists for inputs (insert inputs)
    name = []
    score = []
    for i in range(int(input())):
        name.append(input())
        score.append(float(input()))
    # Create 2D array from names and scores
    l = []
    l.extend([list(a) for a in zip(name, score)])
    # sorts the array in ascending according to  
    # second element 
    l.sort(key = sortSecond)
    # Count the repeated scores
    score.sort() # sort scores
    dic = Counter(score) # count the repititions
    score = list(dict.fromkeys(score)) # remove duplicates
    # Get n that represents the number of students who got 2nd least grad
    # Then save the names of those studens in list out
    out = []
    n = dic[score[1]]
    for i in range(n):
        out.append(l[i+dic[score[0]]][0])
    # Print the names in alphabitical order
    out.sort()
    for i in out:
        print(i)