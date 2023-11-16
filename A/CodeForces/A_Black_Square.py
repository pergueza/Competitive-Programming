calories = list(map(int, input().split()))
s = input()
total = 0

for i in s:
    total += calories[int(i)-1]

print(total)