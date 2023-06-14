import sys
# 입력값 받기
# 케이스마다 리스트로 받아서 리스트에 넣기 - 2차원 배열
C = int(input())
total = []
for _ in range(C):
    total.append(list(map(int, sys.stdin.readline().split())))

# total 리스트를 돌면서 각 배열의 평균값을 구하고, 비율을 구한다
for case in total:
    # 평균값 = 각 배열 안에서 1번째부터 마지막까지의 합을 0번째 인덱스로 나눈다
    case_avg = (sum(case) - case[0]) / case[0]
    # 평균을 넘는 학생들의 비율 : 평균값보다 큰 점수를 count, 0번째 인덱스로 나눈다
    over_avg_count = 0
    for i in range(1, len(case)):
        if case[i] > case_avg:
            over_avg_count += 1
        else:
            continue
    over_avg_rate = over_avg_count / case[0] * 100
    # 각 줄의 비율을 round함수로 소수점 셋째 자리까지 반올림하여 출력한다
    print(format(round(over_avg_rate, 3), ".3f"),'%', sep='')