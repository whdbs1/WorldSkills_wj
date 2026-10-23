x,y = 3,3
sm,em = '007654321','123456700'

aro = {0:[3,1],1:[4,0,2],2:[5,1],3:[0,6,4],4:[1,7,3,5],5:[2,8,4],6:[3,7],7:[4,6,8],8:[5,7]}
ze = {sm:[i for i in range(9) if sm[i] == '0']}

def srh(m):
    res = []
    for i in ze[m]:
        for c in aro[i]:
            if m[c] == '0':
                continue
            cm = list(m)
            cm[i],cm[c] = cm[c],cm[i]
            res.append(''.join(cm))
    return res

def arrow(n):  # 3x3 상하좌우
    li = []
    if n-3 >= 0:
        li.append(n-3)        
    if n+3 < 9:
        li.append(n+3)
    if n%3 != 0:
        li.append(n-1)
    if n%3 != 2:
        li.append(n+1)
    return li

A = {}
for i in range(9):
    A[i] = arrow(i)


for i in A: print(i,':',A[i])

print(arrow(0))
print(A[0])
