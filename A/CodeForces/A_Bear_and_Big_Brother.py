a, b = map(int, input().split())
contador = 0

while not a > b:
    contador += 1
    a *= 3
    b *= 2
print(contador)
