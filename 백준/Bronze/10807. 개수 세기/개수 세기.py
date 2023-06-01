# 입력받기
n = int(input())
num_list = list(map(int, input().split()))
v = int(input())

# 리스트에서 v 찾기
answer = 0
for i in num_list:
    if i == v:
        answer += 1
    
print(answer)