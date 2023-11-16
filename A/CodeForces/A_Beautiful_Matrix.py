lista = []
for i in range(5):
    lista.append(list(map(int, input().split())))

i = 0

for row in lista:
    i += 1
    j = 0
    for element in row:
        j += 1
        if element == 1:
            print(abs(i-3) + abs(j-3))