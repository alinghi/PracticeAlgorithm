N,M,T=map(int,input().split())
circle=[list(map(int,input().split())) for _ in range(N)]
circle_original=[row[:] for row in circle]
orders=[list(map(int,input().split())) for _ in range(T)]


def rotate(circle_row,d,k):
    circle_row-=1
    circle[circle_row]=circle[circle_row][M-k:]+circle[circle_row][:M-k] if d==0 else circle[circle_row][k:]+circle[circle_row][:k]
def whole_rotate(x,d,k):
    x_list=[i for i in range(1,N+1) if i%x==0]
    for xx in x_list:
        rotate(xx,d,k)

def inner():
    l=[[False]*M for _ in range(N)]
    flag=False
    for i in range(N):
        for j in range(M-1):
            if circle[i][j]!=0 and circle[i][j]==circle[i][j+1]:
                l[i][j],l[i][j+1]=True,True
                flag=True
        if circle[i][0]!=0 and circle[i][0]==circle[i][-1]:
            l[i][0], l[i][-1] = True, True
            flag=True
    for i in range(N-1):
        for j in range(M):
            if circle[i][j]!=0 and circle[i][j]==circle[i+1][j]:
                l[i][j],l[i+1][j]=True,True
                flag=True
    if flag:
        for i in range(N):
            for j in range(M):
                if l[i][j]:
                    circle[i][j]=0
    else:
        cnt,SUM=0,0
        for i in range(N):
            for j in range(M):
                if circle[i][j]>0:
                    cnt+=1
                    SUM+=circle[i][j]
        try:
            avg=SUM/cnt
        except:
            avg=0
        for i in range(N):
            for j in range(M):
                if 0<circle[i][j]<avg:
                    circle[i][j]+=1
                elif avg<circle[i][j]:
                    circle[i][j]-=1


def doThis():
    for order in orders:
        whole_rotate(order[0],order[1],order[2])
        inner()
        ans=sum(list(map(sum,(row for row in circle))))
    print(ans)
doThis()