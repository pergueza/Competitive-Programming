n, x = map(int, input().split())
distressed = 0

for i in range(n):
    s, d = map(str, input().split())
    if s == "+":
        x += int(d)
    else:
        if x >= int(d):
            x -= int(d)
        else:
            distressed += 1

print(x, distressed)
    