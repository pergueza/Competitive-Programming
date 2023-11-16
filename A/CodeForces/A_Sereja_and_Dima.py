n = int(input())
cards = list(map(int, input().split()))
sereja = 0
dima = 0

for i in range(n):
    if cards[0] >= cards[-1]:
        if i % 2 == 0:
            sereja += cards[0]
        else:
            dima += cards[0]
        cards.pop(0)
    else:
        if i % 2 == 0:
            sereja += cards[-1]
        else:
            dima += cards[-1]
        cards.pop(-1)
print(sereja, dima)
