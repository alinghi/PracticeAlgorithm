import sys
input=sys.stdin.readline
dr,dc=(0,0,1,-1),(1,-1,0,0)
N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
def BFS(row,col,visit):
    frontier=[(row,col)]
    while frontier:
        next=[]
        for r,c in frontier:
            for dir in range(4):
                nr,nc=r+dr[dir],c+dc[dir]
                if 0<=nr<N and 0<=nc<M and not visit[nr][nc]:
                    if board[nr][nc]<=0:
                        board[r][c]-=1
                    else:
                        visit[nr][nc]=True
                        next.append((nr,nc))
        frontier=next
    return 1
def solution():
    t=0
    while True:
        cc=0
        visit=[[False]*M for _ in range(N)]
        for row in range(N):
            for col in range(M):
                if board[row][col]>0 and not visit[row][col]:
                    if cc==2:
                        return t
                    visit[row][col]=True
                    BFS(row,col,visit)
                    cc+=1
        if cc==0:
            return 0
        elif cc>1:
            return t
        t+=1

print(solution())