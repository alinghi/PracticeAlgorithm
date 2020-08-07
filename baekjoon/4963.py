#Connectivity both hori+verti+diagon
import collections
dx=[0,1,0,-1,1,-1,1,-1]
dy=[1,0,-1,0,1,1,-1,-1]
def BFS(w,h,x,y,m,l):
    def isRange(x,y):
        if 0<=x<h and 0<=y<w:
            return True
        else:
            return False
    de=collections.deque()
    de.append([x,y])
    l[x][y]=m
    while de:
        z=de.popleft()
        for i in range(8):
            mx,my=z[0]+dx[i],z[1]+dy[i]
            if isRange(mx,my):
                if l[mx][my]==1:
                    de.append([mx,my])
                    l[mx][my]=m
    return 1
def island(w,h):
    l=[]
    ans=0
    m=2
    for _ in range(h):
        l.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if l[i][j]==1:
                ans+=BFS(w,h,i,j,m,l)
                m+=1
    print(ans)
    return

def solver():
    w,h=-1,-1
    while True:
        w, h = map(int, input().split())
        if w==0 and h==0:
            break
        island(w,h)
    return
solver()