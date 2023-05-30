x = int(input())
n = int(input())
acc = 0

for i in range(n):
    a, b = map(int, input().split())
    acc = acc + (a * b)
    
if x == acc :
    print('Yes')
else:
    print('No')