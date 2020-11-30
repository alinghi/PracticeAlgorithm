N,M=map(int,input().split())
l=[list(input()) for _ in range(N)]
def cut(board,sr,sc,fr,fc):
    ret=[[board[row][col] for col in range(sc,fc)] for row in range(sr,fr)]
    return ret
def cnt(ret):
    first=ret[0][0]
    second="W" if first=="B" else "B"
    ans1=0
    ans2=0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and ret[i][j]==second:
                ans1+=1
            elif (i+j)%2==1 and ret[i][j]==first:
                ans1+=1
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0 and ret[i][j]==first:
                ans2+=1
            elif (i+j)%2==1 and ret[i][j]==second:
                ans2+=1
    return min(ans1,ans2)

final=9e9
for i in range(7,N):
    for j in range(7,M):
        a=cut(l,i-7,j-7,i+1,j+1)
        final=min(cnt(a),final)
print(final)