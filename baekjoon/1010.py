def solution(a,b):
    ans=0
    if memo.get((a,b))==None:
        for i in range(b-1,a-2,-1):
            ans+=solution(a-1,i)
        memo[(a,b)]=ans
        return ans
    else:
        return memo[(a,b)]

memo=dict()
for i in range(1,30):
    memo[(i,i)]=1
    memo[(1,i)]=i
    if i!=1:
        memo[(2,i)]=i*(i-1)//2
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    print(solution(a,b))
