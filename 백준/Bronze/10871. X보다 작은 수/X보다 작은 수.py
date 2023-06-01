n, x = map(int, input().split())
num_list = list(map(int, input().split()))
ans_list = []

for i in num_list:
    if i < x:
        ans_list.append(i)
    
print(*ans_list)