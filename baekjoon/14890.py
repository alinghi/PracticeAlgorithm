def getRow(x):
    return l[x]
def getCol(x):
    ret=[]
    for i in range(N):
        ret.append(l[i][x])
    return ret

def indicator(l):
    n=[0]*(len(l)+2*L)
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])>1:
            return False
    for i in range(len(l) - 1):
        if l[i]==l[i+1]:
            continue
        elif l[i]+1==l[i+1]:
            for j in range(L):
                n[i-j+L]+=1
        elif l[i]-1==l[i+1]:
            for j in range(L):
                n[i+1+j+L]+=1
    for i in range(L):
        if n[i]>0 or n[-i-1]>0:
            return False
    if max(n)>1:
        return False
    return True

N,L=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
ans=0
for i in range(N):
    ans+=indicator(getCol(i))
for i in range(N):
    ans+=indicator(getRow(i))
print(ans)