def solution(N,M):
    if M>N//2:
        M=N-M
    if l.get((N,M))!=None:
        return l[(N, M)]
    else:
        ans = solution(N - 1, M) + solution(N - 1, M - 1)
    l[(N,M)]=ans%10007
    return ans%10007

N,M=map(int,input().split())
l=dict()
for i in range(1,1001):
    l[(i,0)]=1
    l[(i,1)]=i
    l[(i,2)]=i*(i-1)//2
    l[(i,3)]=i*(i-1)*(i-2)//6
print(solution(N,M))