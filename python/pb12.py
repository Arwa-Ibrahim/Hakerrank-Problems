'''
Task: You have a record of N students.
Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values.
The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type.
The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.
--------------------------------------------------------------------------
Sample Input:
              3
              Krishna 67 68 69
              Arjun 70 98 63
              Malika 52 56 60
              Malika
Sample Output:
              56.00
'''
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("%.2f" %avg)