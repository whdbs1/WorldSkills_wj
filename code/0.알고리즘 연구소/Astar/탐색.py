aro = {0:(3,1),1:(4,2,0),2:(5,1),3:(6,4,0),4:(7,5,1,3),5:(8,2,4),6:(7,3),7:(8,4,6),8:(5,7)}
n = {}
x,y = 3,3
si = x*y
def ecg(m,s,e,r):
    m = list(m)
    m[s],m[e] = m[e],m[s]
    info = [r,int(m[s])]
    return [''.join(m),info]

def srh(m):
    res = []
    if m not in n:
        n[m] = [i for i, v in enumerate(m) if v != '0']
    for i in n[m]:
        q = [i]
        r = {i:[i]}
        for cur in q:
            for j in aro[cur]:
                if j in q or m[j]!='0':
                    continue
                q.append(j)
                r[j] = r[cur] + [j]
                print(r[j])
                res.append(ecg(m,j,i,r[j]))
    return res

