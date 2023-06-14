# 과목 평점 표
grade_score = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

# 입력 값 과목명, 학점, 등급 20줄
import sys

# 학점 리스트, 성적 리스트 추가하기
credit_list = []
score_list = []
for _ in range(20):
    # 입력 받을 때마다 학점은 학점 리스트, 등급은 평점으로 치환하여 성적 리스트에 추가
    # 각각의 자료형이 다르기 때문에 map()을 사용할 수 없음. 공백을 기준으로 split()하여 할당하기
    # 등급이 P인 경우 추가하지 않음
    subject, credit, grade = sys.stdin.readline().rstrip().split(' ')
    if grade != 'P':
        credit_list.append(float(credit))
        score_list.append(grade_score[grade])
    else:
        continue

# for문으로 과목별 성적 합하기 - (학점 * 과목평점)의 합
score_sum = 0
for i in range(len(credit_list)):
    score_sum += credit_list[i] * score_list[i]

# 전공평점 = (학점 * 과목평점)의 합 / 학점의 총합
gpa = score_sum / sum(credit_list)

print(format(round(gpa, 6), ".6f"))