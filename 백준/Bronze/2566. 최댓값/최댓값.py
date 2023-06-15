# 입력값 받기 - 9 * 9 크기의 행렬
import sys
nine_matrix = [
    list(map(int, sys.stdin.readline().split())) for _ in range(9)
]

# 최댓값, 최댓값의 위치 출력
# 각 행마다 최대값 찾아서 딕셔너리에 값과 위치 저장해두기
# 그 중 제일 큰 값과 위치 출력하기

# 각 행의 최댓값을 key, 위치 튜플을 value로 하는 값을 저장할 딕셔너리 선언
find_max = {}

# 이중 for문으로 각 행의 최댓값인 경우 find_max에 값을 저장
# 최댓값의 위치를 인덱스가 아닌 '몇 행 몇 열'인지로 출력해야하기 때문에 r, c에 각각 1을 더해준다.
for r in range(9):
    for c in range(9):
        if nine_matrix[r][c] == max(nine_matrix[r]):
            find_max[nine_matrix[r][c]] = (r + 1, c + 1)
        else:
            continue


# 각 행의 최댓값들 중 최댓값을 출력하기
max_list = list(find_max.keys())
print(max(max_list))
# 해당 값의 위치를 공백을 사이에 두고 출력하기
print(find_max[max(max_list)][0], find_max[max(max_list)][1])