import sys
n, m = map(int, sys.stdin.readline().split())
baskets = [0] * n
for i in range(m):
    s, e, ball = map(int, sys.stdin.readline().split())
    for a in range(s - 1, e):
        baskets[a] = ball
print(*baskets)