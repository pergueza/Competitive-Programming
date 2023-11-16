n, maximumSize, sizeWaste = map(int, input().split())
orangeSize = list(map(int, input().split()))
waste = 0
times = 0

for i in range(n):
    if orangeSize[i] > maximumSize:
        continue
    waste += orangeSize[i]
    if waste > sizeWaste:
        waste = 0
        times += 1
print(times)
