M,N=map(int,input().split())
strcmp=lambda a,b: 1 if a>b else 2 if a==b else 3
l1=[list(map(int,input().split())) for _ in range(M)]
def calc(l):
    x=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            x=10*x+strcmp(l[i],l[j])
    return x
def calc2(l):
    x=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                x+=1
    return x
l2=[calc(l) for l in l1]
print(calc2(l2))