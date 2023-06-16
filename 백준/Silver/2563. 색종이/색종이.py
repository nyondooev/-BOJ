# 도화지 그리기
d_paper = [[0]*100 for _ in range(100)]
# 입력값 받기
import sys
# 색종이의 수
c_papers = int(sys.stdin.readline().rstrip())

# 각 색종이의 영역
# 열 : 인덱스 위치1 부터 (위치1 + 9) 까지
# 행 : 인덱스 (91 - 위치2) 부터 (100 - 위치2) 까지 
for i in range(c_papers):
    column, row = map(int, sys.stdin.readline().split())
    # 이중 for문으로 각 행과 열을 돌며 d_paper에 색종이 영역을 표시하기
    for r in range((91 - row), (101 - row)):
        for c in range(column, (column + 10)):
            d_paper[r][c] = 1

# 1로 표시된 부분은 넓이 계산에 포함됨.
# 1칸의 넓이 = 1 = 1의 개수 = 도화지 행렬의 요소의 합 = 넓이
area = 0
for cp in d_paper:
    area += sum(cp)

print(area)