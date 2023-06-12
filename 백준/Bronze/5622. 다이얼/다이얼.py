a = input()

dials = {
    'ABC' : 3 ,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}
time = 0
for i in a:
    for j in dials.keys():
        if i in j:
            time += dials[j]
print(time)