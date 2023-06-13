# 처음부터 입력값을 받아 대문자로 만든다.
word = input().upper()

# 입력값에서 중복을 제거한 리스트를 만든다.
unq = list(set(word))

# 각 문자의 수를 세는 리스트를 만든다.
# unq를 돌면서 해당 문자가 word에 몇 개 있는지를 cnt리스트에 담는다.
cnt = []
for i in unq:
    cnt.append(word.count(i))

# cnt에서 최댓값이 2개 이상인 경우 ?를 출력한다
# 아닌 경우 cnt의 최댓값의 인덱스를 unq에서 찾아 출력한다.
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(unq[cnt.index(max(cnt))])