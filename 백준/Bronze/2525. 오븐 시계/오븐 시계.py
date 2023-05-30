h, m = map(int, input().split())
t = int(input())

h = h + t//60
m = m + t%60
    
if 59 < m:
    h = h + 1
    m = m - 60
if 23 < h:
    h = h - 24     
    
print(h, m)