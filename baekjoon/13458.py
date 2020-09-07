N=int(input())
ans=0
l=list(map(int,input().split()))
B, C=map(int,input().split())
for i in l:
    i=i-B
    ans=ans+1
    if i>0:
        if i%C==0:
            ans=ans+i//C
        else:
            ans=ans+i//C+1
print(ans)