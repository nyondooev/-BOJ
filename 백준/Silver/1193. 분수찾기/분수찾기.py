# 짝수 라인 : 라인 수만큼 분자 늘어남, 분모 줄어듦
# 홀수 라인 : 라인 수만큼 분모 늘어남, 분자 줄어듦
# 1. 위치 찾기
# 2. 해당 위치의 방향 찾기(짝수라인인지, 홀수라인인지)

X = int(input())
line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    numer = X
    denomi = line - X + 1
else:
    numer = line - X + 1
    denomi = X

print(numer,'/',denomi,sep="")