N=int(input())
#let l=[strength,weight]
#determinant: broken eggs: strength<=0
strength={}
weight={}
for i in range(N):
    strength[i],weight[i]=map(int,input().split())
ans=0
def collision(i,j):
    t=0
    strength[i]-=weight[j]
    strength[j] -= weight[i]
    if strength[i]<=0:t+=1
    if strength[j] <= 0: t += 1
    return t
def egg(left,cnt):
    global ans
    if left==N:
        ans=max(ans,cnt)
        return
    if strength[left]<=0:
        return egg(left+1,cnt)
    for i in range(N):
        if i==left or strength[i]<=0: continue
        strength_i,strength_left=strength[i],strength[left]
        egg(left+1,cnt+collision(left,i))
        strength[i], strength[left]= strength_i, strength_left
    ans=max(ans,cnt)
egg(0,0)
print(ans)