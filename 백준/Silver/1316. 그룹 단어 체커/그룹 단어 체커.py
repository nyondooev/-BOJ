# 1. 입력값 받기
import sys
N = int(sys.stdin.readline().rstrip())
# 값을 입력받으면서 그룹 단어인지 검사한다.
# 그룹 단어 개수를 셀 변수 g_count를 선언하고 0으로 초기화한다.
g_count = 0
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    # 단어 안에서 연속되는 글자를 그룹으로 잘라 리스트에 추가한다.
    # 연속 그룹을 담을 빈 리스트 group_list를 선언한다.
    group_list = []
    # 반복문으로 단어 내부를 돌면서, 각 글자 하나씩 리스트에 추가
    # 반복되는 글자는 그룹에 하나만 추가되게 됨
    for i in range(len(word)):
        if i == 0:
            group_list.append(word[i])
        elif word[i] == word[i - 1]:
            continue
        else:
            group_list.append(word[i])
    # 그룹 리스트에서 중복되는 값이 있으면 그룹 단어가 아님,
    # 중복 값이 없다면 그룹 단어이므로 g_count + 1
    # 중복 체크용 빈 리스트 check_rep 을 선언한다.
    check_rep = []
    for g in group_list:
        if g in check_rep:
            continue
        else:
            check_rep.append(g)
    # 반복문이 끝나고, check_rep의 길이와 group_list의 길이를 비교한다.
    # 길이가 같으면 그룹 단어, 다르면 그룹 단어 아님
    if len(check_rep) == len(group_list):
        g_count += 1

print(g_count)