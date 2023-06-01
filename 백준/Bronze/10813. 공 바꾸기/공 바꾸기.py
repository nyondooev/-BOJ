import sys
n, m = map(int, sys.stdin.readline().split())
baskets = [0] * n
save = 0

for a in range(n):
    baskets[a] = a + 1
    
for b in range(m):
    i, j = map(int, sys.stdin.readline().split())
    save = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = save

print(*baskets)