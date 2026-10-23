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
                res.append(''.join(cm))
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

def dfs(m, em, g, lm, path):
    f = g + hg(m, em)
    if f > lm:
        return f
    if m == em:
        return path[:]
    min_bound = float('inf')
    for cm in srh(m):
        if cm in path:
            continue
        path.append(cm)
        result = dfs(cm,em,g+1,lm,path)
        if isinstance(result, list):
            return result
        path.pop()
        min_bound = min(min_bound, result)

    return min_bound

def ida_star(sm, em):
    lm = hg(sm, em)

    while True:
        result = dfs(sm, em, 0, lm, [sm])

        if isinstance(result, list):
            return result

        if result == float('inf'):
            return None

        lm = result

sm, em ='007654321', '123456700'


st = time.time()
ida_star(sm, em)
et = time.time()
res = et - st


print("실행 시간: {:.5f}초".format(res))
        
