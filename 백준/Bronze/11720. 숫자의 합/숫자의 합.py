import sys
N = int(sys.stdin.readline().rstrip())
str_lst = list(sys.stdin.readline().rstrip())
ans = 0
for i in range(N):
    ans += int(str_lst[i])
    
print(ans)