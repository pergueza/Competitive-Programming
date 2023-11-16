s = input().split("+")
s.sort()
for i in range(len(s)):
    print(s[i], end="+") if i!=len(s)-1 else print(s[i])