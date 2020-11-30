def onestar(n):
    for _ in range(n):print(" ",end="")
    print("*")
def twostar(n,b):
    for _ in range(n):print(" ",end="")
    print("*",end="")
    for _ in range(b): print(" ", end="")
    print("*")

N=int(input())
onestar(N-1)
for i in range(1,N):
    twostar(N-1-i,2*i-1)