N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
for H,W,N in l:
    print(str(H if N%H==0 else N%H)+str(N//H+1- (1 if N%H==0 else 0)).zfill(2))