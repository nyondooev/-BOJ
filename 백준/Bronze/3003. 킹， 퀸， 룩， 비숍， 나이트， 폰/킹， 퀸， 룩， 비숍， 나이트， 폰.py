# 올바른 개수 리스트 할당하기
origin = [1, 1, 2, 2, 2, 8]
# 입력값 받아서 리스트로 형변환
cur = list(map(int, input().split()))

# 올바른 개수 - 현재값(입력값) = 더하거나 빼야 할 개수
for i in range(len(origin)):
    print(origin[i] - cur[i], end = ' ')