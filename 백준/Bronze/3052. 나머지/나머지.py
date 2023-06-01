# 10개 입력받기
# 42로 나눈 나머지 리스트에 넣기
# 중복 제거하기
# 그 리스트 요소 개수 출력하기
import sys

rest = []
for i in range(10):
    num = int(sys.stdin.readline().strip())
    if num % 42 not in rest:
        rest.append(num % 42)

print(len(rest))