n = int(input())
s = input()
total = 0
anterior = ""

for j in s:
    if anterior == j:
        total += 1
    anterior = j
print(total)