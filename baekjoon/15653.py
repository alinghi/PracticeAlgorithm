import collections
N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
dr=[0,0,-1,1]
dc=[1,-1,0,0]
for i in range(N):
    for j in range(M):
        if l[i][j]=="R":
            red_r,red_c=i,j
        elif l[i][j]=="B":
            blue_r,blue_c=i,j
check=[[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
check[red_r][red_c][blue_r][blue_c]=True
def move(r,c,dr,dc):
    cnt=0
    while l[r+dr][c+dc]!='#'and l[r][c]!='O':
        r=r+dr
        c=c+dc
        cnt+=1
    return r,c,cnt

def BFS(red_r,red_c,blue_r,blue_c):
    de = collections.deque()
    de.append((red_r,red_c,blue_r,blue_c,0))
    while de:
        red_r,red_c,blue_r,blue_c,distance=de.popleft()
        for k in range(4):
            nred_r,nred_c,red_distance=move(red_r,red_c,dr[k],dc[k])
            nblue_r, nblue_c, blue_distance = move(blue_r, blue_c, dr[k], dc[k])
            if l[nblue_r][nblue_c]=='O':
                continue
            if l[nred_r][nred_c]=='O':
                print(distance+1)
                return
            if nred_r==nblue_r and nred_c==nblue_c:
                if red_distance>blue_distance:
                    nred_r-=dr[k]
                    nred_c -= dc[k]
                else:
                    nblue_r-=dr[k]
                    nblue_c-=dc[k]
            if not check[nred_r][nred_c][nblue_r][nblue_c]:
                check[nred_r][nred_c][nblue_r][nblue_c]=True
                de.append((nred_r,nred_c,nblue_r,nblue_c,distance+1))
    print(-1)
BFS(red_r,red_c,blue_r,blue_c)