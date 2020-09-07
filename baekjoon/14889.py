N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
ans=9e9
def score(t):
    ret=0
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            ret+=l[t[i]][t[j]]
            ret+=l[t[j]][t[i]]
    return ret
def team(N,current):
    global ans
    if len(current)==N//2:
        t1=[]
        t2=[]
        for i in range(N):
            if i in current:
                t1.append(i)
            else:
                t2.append(i)
        ans=min(abs(score(t1)-score(t2)),ans)
        return
    if len(current)==0:
        for i in range(N):
            current.append(i)
            team(N,current)
            current.pop()
    else:
        for i in range(current[-1]+1,N):
            current.append(i)
            team(N,current)
            current.pop()
    return

team(N,[])
print(ans)