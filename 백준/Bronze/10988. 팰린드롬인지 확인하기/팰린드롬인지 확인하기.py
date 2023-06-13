word = input()

# 단어를 반으로 나눠서 양 옆이 같으면 펠린드롬으로 간주
# 단어의 길이를 2로 나눈 몫 만큼 양 옆을 잘라서 비교하기
if word[::-1] == word:
    print(1)
else:
    print(0)