wires = int(input())
birds = list(map(int, input().split()))
shots = int(input())

for i in range(shots):
    x, y = map(int, input().split())
    x -= 1
    if x == 0 and x == wires-1:
        birds[x] = 0
    elif x == 0:
        birds[x+1] += birds[x] - y
        birds[x] = 0
    elif x == wires-1:
        birds[x-1] += y-1
        birds[x] = 0
    else:
        birds[x-1] += y-1
        birds[x+1] += birds[x] - y
        birds[x] = 0

for wire in birds:
    print(wire)
    
