import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    ans = ''
    for a in S:
        ans += a*int(R)
    print(ans)