n = int(input())
s = list(map(int, input().split()))
x = 0
total = 0

for i in range(n):
    if s[i] >= 0:
        x += s[i]
    elif x > 0:
        x -= 1
    else:
        total += 1
print(total)