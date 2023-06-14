# 입력값 받기
import sys
N, M = map(int, sys.stdin.readline().split())

# N * M 크기의 행렬
# N = 행, M = 열 : 길이가 M인 행렬 N개가 있는 2차원 배열
A = []
for a in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
B = []
for b in range(N):
    B.append(list(map(int, sys.stdin.readline().split())))

# 행렬 A와 B를 더한다.
# for문으로 각 위치에 맞는 요소를 더한다
# 각 행에서 열 별로 더하기
# N*M크기의 빈 행렬 만들기
sum_matrix = [[0] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        sum_matrix[n][m] = A[n][m] + B[n][m]
    print(*sum_matrix[n])