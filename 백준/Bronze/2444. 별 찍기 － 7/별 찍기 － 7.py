N = int(input())

# 규칙
# (2*N - 1) // 2 번째까지는 늘어남
# 2*N - 1 개
# 거꾸로
for i in range(1, 2*N):
    if i <= (2*N-1)//2:
        print(' ' * (N - i) + '*' * (i*2 - 1))
    elif i == (2*N-1)//2+1:
        print('*' * (2*N-1))
    else:
        print(' ' * (i - N) + '*' * (abs(i - (2*N-1)) * 2 + 1))