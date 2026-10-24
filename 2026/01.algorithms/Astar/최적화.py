import heapq
def aro(n):
    if n in ser:
        return ser[n]
    res=[]
    dy,dx=[-1,0,1,0],[0,1,0,-1]
    y,x,z=(n//sx)%sy,n%sx,n//(si)
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if -1<ny<sy and -1<nx<sx:
            res.append(ny*sx+nx+z*si)
    ser[n]=res
    return res

def srh(m):
    if m not in num:
        num[m] = [i for i in range(si) if m[i]!='0']
    res = []
    for i in num[m]:
        v = [i]
        r = {i:[i]}
        for cur in v:
            for j in aro(cur):
                if j in v or m[j]!='0':
                    continue
                v.append(j)
                r[j] = r[cur] +[j]
                cm = list(m)
                cm[j],cm[i] = cm[i],cm[j]
                res.append([''.join(cm),[r[j],int(m[i])]])
    return res
                
def hg(m,em):
    res = 0
    if m not in num:
        num[m] = [i for i in range(9) if m[i]!='0']
    for i in num[m]:
        j = em.index(m[i])
        x1,y1 = (i//sx, i%sx)
        x2,y2 = (j//sx, j%sx)
        res += abs(x1-y1) + abs(x2-y2)
    return res                

def main():
    global ser,num,sx,sy,sz,si
    sx,sy,sz = 3,3,1
    sm,em = '007654321','123465700'
    si = sx*sy
    ser = {}
    num = {}
    ol = [(hg(sm, em), 0, sm)]
    cl = {sm:0}
    par = {}

    while ol:
        f, g, cur = heapq.heappop(ol)
        if cl[cur] != g:
            continue
        if cur == em:
            path = []
            while cur != sm:
                s,e = par[cur]
                path.append([cur,e])
                cur = s
            path.reverse()
            return path
        ng = g + 1
        for cm,st in srh(cur):
            if cm not in cl:
                cl[cm] = ng
                par[cm] = (cur,st)
                heapq.heappush(ol, (hg(cm, em) + ng, ng, cm))

    return None


