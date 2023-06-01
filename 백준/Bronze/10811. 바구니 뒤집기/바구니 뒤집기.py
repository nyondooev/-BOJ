import sys
n, m = map(int, sys.stdin.readline().split())
# 처음 상태의 바구니
baskets = [0] * n
for a in range(n):
    baskets[a] = a + 1
# 바구니 바꾸기
for b in range(m):
    i, j = map(int, sys.stdin.readline().split())
    change_b = []
    for c in range(i - 1, j):
        change_b.append(baskets[c])
    change_b.reverse()
    baskets[i - 1:j] = change_b

print(*baskets)