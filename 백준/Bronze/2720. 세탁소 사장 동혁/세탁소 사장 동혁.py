# 입력값 받기
import sys
T = int(sys.stdin.readline().rstrip())

# 각 테스트 케이스별로 거스름돈 출력
for _ in range(T):
    Quarter, Dime, Nickel, Penny = 0, 0, 0, 0
    C = int(sys.stdin.readline().rstrip())
    Quarter = (C // 25)
    Dime = (C % 25) // 10
    Nickel = (C % 25) % 10 // 5
    Penny = (C % 25) % 10 % 5
    print(Quarter, Dime, Nickel, Penny)