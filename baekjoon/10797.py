N=int(input())
x=lambda z:1 if int(z)==N else 0
print(sum(map(x,input().split())))