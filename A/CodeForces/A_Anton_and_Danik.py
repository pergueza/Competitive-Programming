n = int(input())
a = list(input())

if a.count("A") > a.count("D"):
    print("Anton")
elif a.count("A") < a.count("D"):
    print("Danik")
else:
    print("Friendship")
