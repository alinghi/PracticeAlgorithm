import collections
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def isRange(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False
def BFS(x,y,m,n):
    ans=1
    de=collections.deque()
    de.append([x,y])
    l[x][y]=m
    while de:
        z=de.popleft()
        for i in range(4):
            mx,my=z[0]+dx[i],z[1]+dy[i]
            if isRange(mx,my,n):
                if l[mx][my]==1:
                    de.append([mx,my])
                    l[mx][my]=m
                    ans += 1
    return ans
def init():
    n=int(input())
    l=[]
    for _ in range(n):
        l.append(list(map(int,input())))
    return n,l

def solver(n,l):
    cnt=2
    for i in range(n):
        for j in range(n):
            if l[i][j]==1:
                x=BFS(i,j,cnt,n)
                ret.append(x)
                cnt+=1
    ret.sort()
    print(len(ret))
    for i in ret:
        print(i)


n,l = init()
ret=[]
solver(n,l)