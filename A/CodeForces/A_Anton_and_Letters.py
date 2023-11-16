s = input()
x = s[1:-1].split(", ")
x.sort()
total = 0
anterior = ""

for i in range(len(x)):
    if x[i] != anterior:
        total += 1
    anterior = x[i]
    
print(total)