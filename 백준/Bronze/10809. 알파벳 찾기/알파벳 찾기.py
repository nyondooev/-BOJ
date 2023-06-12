s = input()
alpah = list('abcdefghijklmnopqrstuvwxyz')
for i in alpah:
    if i in s:
        ans = s.index(i)
    else:
        ans = -1
    print(ans ,end = " ")