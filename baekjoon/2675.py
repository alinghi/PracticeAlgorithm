N=int(input())
def solution():
    N,s=input().split()
    N=int(N)
    S="".join(z*N for z in s)
    print(S)
for _ in range(N):
    solution()