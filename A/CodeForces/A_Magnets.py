n = int(input())
anterior = 0
total = 0

for x in range(n):
    i = int(input())
    if i != anterior:
        total+=1
    anterior = i

print(total)