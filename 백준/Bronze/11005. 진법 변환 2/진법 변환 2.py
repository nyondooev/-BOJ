# 자릿수 변환 딕셔너리
digits = {
    10: 'A', 11: 'B', 12: 'C', 
    13: 'D', 14: 'E', 15: 'F',
    16: 'G', 17: 'H', 18: 'I', 
    19: 'J', 20: 'K', 21: 'L',
    22: 'M', 23: 'N', 24: 'O', 
    25: 'P', 26: 'Q', 27: 'R',
    28: 'S', 29: 'T', 30: 'U', 
    31: 'V', 32: 'W', 33: 'X',
    34: 'Y', 35: 'Z'
}

# 입력값 받기
N, B = map(int, input().split())

# 숫자를 담을 리스트 선언하기
change_num = []
# 주어진 10진법 숫자를 B로 나눈다. 몫이 0보다 클때동안
# 몫과 나머지 -> 나머지는 저장, 몫은 계속 나누기
# 마지막 몫을 리스트에 넣어준다.
while N // B > 0:
    change_num.append(N % B)
    N = N // B
    
change_num.append(N)

# 최종 숫자는 나열해야한다.
for n in range(len(change_num)):
    if change_num[n] in digits.keys():
        change_num[n] = digits[change_num[n]]
    else:
        continue
    
print(*reversed(change_num), sep="")