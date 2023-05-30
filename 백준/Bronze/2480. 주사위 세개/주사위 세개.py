dice = list(map(int, input().split()))

if dice[0] == dice[1] and dice[1] == dice[2]:
    p = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[1] == dice[2]:
    p = 1000 + dice[1] * 100
elif dice[0] == dice[2]:
    p = 1000 + dice[2] * 100
else:
    p = max(dice)*100
print(p)