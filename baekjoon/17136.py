MAX=10
l=[list(map(int,input().split())) for _ in range(MAX)]
ans=9e9
cnt=0
paper=[0,5,5,5,5,5]
def func(row,col):
    global cnt
    if col==MAX:
        func(row+1,0)
        return
    if row==MAX:
        global ans
        ans=min(ans,cnt)
        return
    if l[row][col]==0:
        func(row,col+1)
        return
    for len in range(5,0,-1):
        if paper[len]==0 or row+len>MAX or col+len>MAX:
            continue
        flag=True
        for i in range(len):
            for j in range(len):
                if l[row+i][col+j]==0:
                    flag=False
                    break
            if not flag:
                break
        if not flag:
            continue
        for i in range(len):
            for j in range(len):
                l[row+i][col+j]=0
        paper[len]-=1
        cnt+=1
        func(row,col+len)
        for i in range(len):
            for j in range(len):
                l[row+i][col+j]=1
        paper[len]+=1
        cnt-=1

func(0,0)
if ans==9e9:
    print(-1)
else:
    print(ans)
