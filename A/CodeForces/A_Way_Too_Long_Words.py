n = int(input())
for i in range(n):
    s = input()
    if len(s) > 10:
        print("{}{}{}".format(s[0], len(s)-2,s[-1]))
    else:
        print(s)