def solution(N,M):
    if N<M:
        N,M=M,N
    if M==1:
        return N-1
    if N%2==0:
        return solution(N//2,M)+solution(N//2,M)+1
    else:
        return solution(N // 2, M) + solution(N // 2+1, M) + 1
N,M=map(int,input().split())
print(solution(N,M))