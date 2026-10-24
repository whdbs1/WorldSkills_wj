import heapq
from time import time
def ecg(m,s,e,r):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    info = [r,int(m[s])]
    return [''.join(m),info]

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

def cs(m):
    res = []
    for i in range(si):
        if m[i] in ('0','x','h'):
            continue
        q = [i]
        r = {i: [i]}
        for cur in q:
            for j in aro(cur):
                if j in r or m[j] not in ('0','h'):
                    continue
                q.append(j)
                r[j] = r[cur] + [j]
                if m[j] == '0':
                    res.append(ecg(m, j, i, r[j]))

    return res

def H(m):
    ct = 0
    for i in range(si):
        if leaf[i] not in '0x':
            if m[i]==leaf[i]:
                ct-=5
    return ct

def C(g,m,*a):
    global t,sx,sy,sz,si,ser,leaf,res
    sy,sx,sz = 7,3,1
    si = sy*sx
    ser = {}

    t=g
    ser = {}
    res = []
    leaf, = a
    q = []
    mli = {m:[m]}
    st = {m:0}
    ph = lambda c: heapq.heappush(q,(st[c]**[1,1,1][t]+H(c),c))
    ph(m)
    while 1:
        c = heapq.heappop(q)[1]
        if c == leaf:
            break
        for i,j in cs(c):
            if i not in mli:
                mli[i] = mli[c]+[j]
                st[i]=st[c]+1
                ph(i)
    res+=mli[c][1:]
    return res


if __name__ == '__main__':
    t = 0
    if t == 0:
        m,leaf ='xx65000x93700x1248xx', 'xx14700x25800x36900xx'
    ts = time()
    res = C(t,m,leaf)
    te = time() - ts
    print(res)
    print("{}step, idle {}s(DART-Studio {}m {}s) \n".format(len(res),round(te,3),int((te*250)//60),int((te*250)%60)))

