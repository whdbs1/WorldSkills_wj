sx,sy = 7,3
ser = {}

def aro(n):
    if n in ser:
        return ser[n]
    res=[]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    y,x=(n//sx)%sy,n%sx
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if -1<ny<sy and -1<nx<sx:
            res.append(ny*sx+nx)
    ser[n]=res
    return res
def peck_(em):
    numbering = [6,14,15,5,12,8]
    Em = em
    log = []
    for i in numbering:
        if Em[i] not in ('0','x'):
            log.append(Em[i])
            continue
        visited = [i]
        while True:
            k = visited[0]
            del visited[0]
            for j in aro(k):
                if Em[j] == '0':
                    visited.append(j)
                elif Em[j] != 'x' and Em[j] not in log:
                    log.append(Em[j])
                    Em = list(Em)
                    Em[i],Em[j] = Em[j],Em[i]
                    Em = ''.join(Em)
                    break
            else: continue
            break
    return Em
def H(m):
    ct = 0
    for i in [6,14,15,5,12,8]:
        print(e[i])
##        if leaf[i] not in '0x':
##                if m[i]==e[i]:
##                    ct-=5  
##    return ct

e = peck_('xx00000x09876x54321xx')
'''
xx00076
x90801x
54320xx

xx12345
x67890x
00000xx
'''
