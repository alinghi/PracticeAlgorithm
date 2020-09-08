N,M=map(int,input().split())
def solution(N,M):
    level=[{N:True},{}]
    time = 0
    frontier=[N]
    while frontier:
        next=[]
        M = M + time
        if M in level[time%2]:
            return time
        if M>500000:
            return -1
        time = time + 1
        for u in frontier:
            for v in [u-1,u+1,2*u]:
                if 0<=v<500001:
                    if v not in level[time%2]:
                        level[time%2][v]=True
                        next.append(v)
        frontier=next

print(solution(N,M))