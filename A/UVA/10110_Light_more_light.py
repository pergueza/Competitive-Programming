import math

n = int(input())


while n != 0:
    x = math.sqrt(n)
    if (int(x)*int(x)) == n:
        print("yes")
    else:
        print("no")
    n = int(input())
