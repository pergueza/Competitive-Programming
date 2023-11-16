n = int(input())
total = 0

for i in range(n):
    l = list(map(int, input().split()))
    if l.count(1) > 1:
        total +=1
print(total)
