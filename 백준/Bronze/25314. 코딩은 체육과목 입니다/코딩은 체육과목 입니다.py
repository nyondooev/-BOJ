n = int(input())

if n % 4 == 0:
    ans = 'long ' * (n // 4) + 'int'
else:
    ans = 'long ' * (n // 4 + 1) + 'int'

print(ans)