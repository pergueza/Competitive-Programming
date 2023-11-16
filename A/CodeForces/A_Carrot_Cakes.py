n, timeBake, bakeCake, timeMakeOven = map(int, input().split())
cake = bakeCake
time = timeBake
time2 = time
time3 = timeMakeOven

while cake < n:
    cake += bakeCake
    time += timeBake

cake = bakeCake

while cake < n:
    time2 += timeBake
    if time2 > timeMakeOven:
        cake += bakeCake*2
    else:
        cake += bakeCake

cake = 0

while cake < n:
    time3 += timeBake
    cake += bakeCake*2

if time <= min(time2, time3):
    print("NO")
else:
    print("YES")    