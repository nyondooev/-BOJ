# 입력값 받기 - 5 * n 크기의 2차원 배열 입력
import sys
words = [
    list(sys.stdin.readline().rstrip()) for _ in range(5)
]

# 길이가 가장 긴 배열의 길이를 구하기 위한 반복문. 해당 배열의 최댓값을 아래 반복문에 넣어준다.
max_length = []
for i in range(5):
    max_length.append(len(words[i]))

# for문 돌면서 세로로 단어를 더할 때 길이가 짧은 단어는 값이 없기 때문에 index error가 난다.
# 따라서 for문 돌리기 전에 짧은 단어는 max_length와의 차이만큼 빈 문자열을 더해줘서 모든 행의 길이를 max_length에 맞춘다.
for w in words:
    if len(w) < max(max_length):
        for j in range(max(max_length) - len(w)):
            w.append("")

# 이중 for문으로 각 행을 가장 길이가 긴 배열의 길이만큼 돌며 문자열을 더한다.
vertical_read = ""
for c in range(max(max_length)):
    for r in range(5):
        vertical_read += words[r][c]

# 최종적인 단어를 출력한다.
print(vertical_read)