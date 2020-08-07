import sys
sys.setrecursionlimit(987654321)
l=[[0]*(3**7) for _ in range(3**7)]
def solve(x,y,N):
    if N==1:
        l[x][y]=1
        return
    z=N//3
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            else:
                solve(x+i*z,y+j*z,z)
def print_out(N):
    for i in range(N):
        for j in range(N):
            if l[i][j]==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()
N=int(input())
solve(0,0,N)
print_out(N)