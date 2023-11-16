t = int(input())

for i in range(t):
    x, y, k = map(int, input().split())
    if y <= x:
        print(x)
    elif (x+k) >= y:
        print(y)
    else:
        print(x+k+((y-(x+k))*2))
