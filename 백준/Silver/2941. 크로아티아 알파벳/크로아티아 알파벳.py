# 입력값 받기
cra = input()
# 변경 목록 만들기
change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# 변경 목록에 있는 글자가 단어에 있으면 count에 +1하고 지우기
ca_count = 0
for word in change:
    # <변경할 글자를 지울 때 주의할 사항>
    # 변경할 글자를 없앤 후 새롭게 변경할 글자가 되어버리는 경우:
    # 변경 후 새로운 문자조합이 되면 안된다.
    # 공백으로 바꾼다.
    # 변경할 글자가 중복되는 경우:
    # 반복문을 한 번 돌때 해당 문자가 중복이면 그만큼 count를 해준다.
    if word in cra:
        ca_count += cra.count(word)
        cra = cra.replace(word, " ")
    else:
        continue
# 남은 단어는 공백을 없앤 후 길이를 count에 더하기
print(ca_count + len(cra.replace(" ", '')))