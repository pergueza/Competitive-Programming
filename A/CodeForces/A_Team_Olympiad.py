n = int(input())
students = list(map(int, input().split()))

prog = students.count(1)
math = students.count(2)
pe = students.count(3)

w = min(prog, math, pe)
print(w)

for i in range(w):
    print(students.index(1)+1, students.index(2)+1, students.index(3)+1)
    students[students.index(1)] = 0
    students[students.index(2)] = 0
    students[students.index(3)] = 0