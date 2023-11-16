k, t = map(int, input().split())
i = 1
k = k%10

while (k*i) % 10 != t:
    if (k*i)%10 == 0:
        break
    i += 1
print(i)
