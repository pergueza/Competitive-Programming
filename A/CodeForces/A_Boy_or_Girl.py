s = input()
total = 0
temp = 0
for letter in s:
    if s.count(letter) == 1:
        total += 1
    else:
        if temp <= s.find(letter) :
            total += 1
    temp += 1
if total % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")