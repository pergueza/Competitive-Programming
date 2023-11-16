s = list(map(int, input().split()))
s.sort()
total = 0

for i in range(3):
    if s[i+1] == s[i]:
        total += 1

print(total)