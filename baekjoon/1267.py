n=int(input())

l=list(map(int,input().split()))
y=lambda x: (x//30)*10+(10 if x%30>=0 else 0)
m=lambda x: (x//60)*15+(15 if x%60>=0 else 0)
yc=sum(map(y,l))
mc=sum(map(m,l))
if yc==mc:
    print("Y M "+str(yc))
elif yc<mc:
    print("Y "+str(yc))
else:
    print("M "+str(mc))