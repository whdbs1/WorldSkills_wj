import time
import heapq
import random
def srh(m):
    global n
    res = []
    if m not in n:
        n[m] = [i for i in range(9) if m[i]!='0']
    for i in n[m]:
        q=[i]
        r={i:[i]}
        for cur in q:
            for j in aro[cur]:
                if j in q or m[j]!='0':
                    continue
                q.append(j)
                r[j] = r[cur] + [j]
                cm = list(m)
                cm[j],cm[i] = cm[i],cm[j]
                res.append([''.join(cm),[r[j],int(m[i])]])
    return res

def hg(m,em):
    global n
    res = 0
    if m not in n:
        n[m] = [i for i in range(9) if m[i]!='0']
    for i in n[m]:
        j = em.index(m[i])
        sx,sy = (i//x, i%x)
        ex,ey = (j//x, j%x)
        res += abs(sx-ex) + abs(sy-ey)
    return res

def main():
    global sm,em,x,y,aro,n
    sm,em = '536071420','123456700'
    x,y = 3,3
    aro = {0: [1]}
{1: [2, 0]}
{2: [3, 1]}
{3: [4, 2]}
{4: [5, 3]}
{5: [6, 4]}
{6: [7, 5]}
{7: [8, 6]}
{8: [9, 7]}
{9: [8]}
    n = {}
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
