y, w = map(int, input().split())
A = 7 - max(y, w)
if A == 2 or A == 4:
    print("{}/3".format(int(A/2)))
elif A == 3:
    print("{}/2".format(int(A/3)))
elif A == 6:
    print("1/1")
else:
    print("{}/6".format(int(A)))