# 10진법 이상 자릿수 목록
digits = {
    'A' : 10, 'B' : 11, 'C' : 12, 
    'D': 13, 'E' : 14, 'F' : 15,
    'G' : 16, 'H' : 17, 'I' : 18, 
    'J' : 19, 'K' : 20, 'L' : 21,
    'M' : 22, 'N' : 23, 'O': 24, 
    'P' : 25, 'Q' : 26, 'R' : 27,
    'S' : 28, 'T' : 29, 'U' : 30, 
    'V' : 31, 'W' : 32, 'X' : 33,
    'Y' : 34, 'Z' : 35
}

# 입력값 받기
N, B = map(str, input().split())

# 리스트로 만들기
input_num = list(N)

# 자리수 * 해당 자리의 숫자 를 합한 것
# 지수 = 인덱스를 반대로
# 10진법 이상인 경우 
decimal = 0
for i in range(len(input_num)):
    if int(B) < 10:
    # 10진법 미만인 경우
        decimal += (int(B) ** (len(input_num) - 1 - i)) * int(input_num[i])
    else:
   # 10진법 이상인 경우
   # digits에 있는 경우 input_num의 요소를 10진법 수로 변환한다.
        if input_num[i] in digits.keys():
            decimal += (int(B) ** (len(input_num) - 1 - i)) * digits[input_num[i]]
        else:
            decimal += (int(B) ** (len(input_num) - 1 - i)) * int(input_num[i])

print(decimal)