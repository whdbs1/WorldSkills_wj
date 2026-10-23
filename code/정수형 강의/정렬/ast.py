import heapq
import time

x,y = 3,3
def srh(m):
    res = []
    for i in range(len(m)):
        if m[i] != '0':
            continue
        sy,sx = divmod(i,x)
        dy,dx = [1,0,-1,0],[0,1,0,-1]
        for j in range(4):
            y1,x1 = sy+dy[j],sx+dx[j]
            if -1<y1<y and -1<x1<x:
                c = y1*x+x1
                if m[c] == '0':
                    continue
                cm = list(m)
                cm[i],cm[c] = cm[c],cm[i]
                res.append([''.join(cm),[c,i]])
    return res

def hg(m,em):
    res = 0
    for i in range(len(m)):
        if m[i] != '0':
            j = em.index(m[i])
            sx,sy = (i//x, i%x)
            ex,ey = (j//x, j%x)
            res += abs(sx-ex) + abs(sy-ey)
    return res

def main(m):
    sm,em = '007654321','123456700'
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
                path.append(e)
                cur = s
            path.reverse()
            return path
        ng = g + 1
        for cm,st in srh(cur):
            if cm not in cl:
##            if cm not in cl or ng < cl[cm]:
                cl[cm] = ng
                par[cm] = (cur,st)
                heapq.heappush(ol, (hg(cm, em) + ng, ng, cm))

    return None

            
st = time.time()
print(main('007654321'))
et = time.time()
res = et - st


print("실행 시간: {:.5f}초".format(res))
