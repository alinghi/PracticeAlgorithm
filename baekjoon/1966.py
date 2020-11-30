tc=int(input())
def solution():
    N,M=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(N):
        l[i]=(l[i],i)
    i=1
    while True:
        m=max(l)[0]
        while l[0][0]!=m:
            l.append(l.pop(0))
        pop=l.pop(0)
        if pop[1]==M:
            return i
        i+=1
for _ in range(tc):
    print(solution())