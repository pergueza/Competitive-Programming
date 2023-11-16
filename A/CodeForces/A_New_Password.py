n, k = map(int, input().split())
distinct = 1
for i in range(n):
    print(chr(96+distinct), end="")
    if distinct < k:
        distinct += 1
    else:
        distinct = 1