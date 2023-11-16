s = input()
total = 0
anterior = 0

for letter in s:
    pasos = abs(ord(letter) - 97 - anterior)
    if pasos > 12:
        total += abs(pasos - 26)
    else:
        total += pasos
    anterior = ord(letter) - 97
print(total)
