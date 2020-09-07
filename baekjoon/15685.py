def init():
    N=int(input())
    l=[list(map(int,input().split())) for _ in range(N)]
    m = [[0] * 101 for _ in range(101)]
    match = [1, 2, 3, 0]
    return N, l, m, match

def dragon():
    pre=[0]
    for i in range(10):
        for j in reversed(pre):
            pre.append(match[j])
    return pre
def solver(l,m):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    def paste(i):
        x,y=i[0],i[1]
        m[x][y]=1
        for k in range(2**i[3]):
            x+=dx[(dra[k]+i[2])%4]
            y+=dy[(dra[k]+i[2])%4]
            m[x][y]=1
    for i in l:
        paste(i)
def cnt(m):
    ret=0
    for i in range(1,101,2):
        for j in range(1,101,2):
            if m[i][j]:
                if m[i-1][j]:
                    if m[i-1][j-1] and m[i][j-1]:
                        ret+=1
                    if m[i-1][j+1] and m[i][j+1]:
                        ret+=1
                if m[i+1][j]:
                    if m[i+1][j-1] and m[i][j-1]:
                        ret+=1
                    if m[i+1][j+1] and m[i][j+1]:
                        ret+=1
    return ret
N,l,m,match=init()
dra=dragon()
solver(l,m)
print(cnt(m))