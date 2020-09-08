import sys
R,C,N=map(int,sys.stdin.readline().split())
l1=[list(sys.stdin.readline().rstrip()) for _ in range(R)]
l2=[["O"]*C for _ in range(R)]
if N<2:
    for i in l1:print("".join(i))
elif N%2==0:
    for i in l2:print("".join(i))
else:
    l3=[["O"]*C for _ in range(R)]
    l4=[["O"]*C for _ in range(R)]
    di,dj=(1,-1,0,0),(0,0,1,-1)
    for i in range(R):
        for j in range(C):
            if l1[i][j]=='O':
                l3[i][j] = "."
                for k in range(4):
                    if 0<=i+di[k]<R and 0<=j+dj[k]<C:
                        l3[i+di[k]][j+dj[k]]="."
    for i in range(R):
        for j in range(C):
            if l3[i][j]=='O':
                l4[i][j] = "."
                for k in range(4):
                    if 0<=i+di[k]<R and 0<=j+dj[k]<C:
                        l4[i+di[k]][j+dj[k]]="."
    if N%4==3:
        for i in l3:print("".join(i))
    elif N%4==1:
        for i in l4:print("".join(i))