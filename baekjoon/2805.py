K,N=map(int,input().split())
q=list(map(int,input().split()))
l,h=0,2**33
while l+1<h:
 m=(l+h)//2
 if sum(i-m if i>m else 0 for i in q)>=N:l=m
 else:h=m
print(l)