n, h = input().split()
a = list(map(int, input().split()))
result = 0

for i in a:
    if i <= int(h):
        result += 1
    else:
        result += 2

print(result)
