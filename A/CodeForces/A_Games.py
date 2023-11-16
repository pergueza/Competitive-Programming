n = int(input())
home = []
guest = []
total = 0

for i in range(n):
    x, y = map(int, input().split())

    home.append(x)
    guest.append(y)

for i in home:
    total += guest.count(i)
    
print(total)
