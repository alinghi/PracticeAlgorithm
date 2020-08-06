K,N=map(int,input().split())
q=[int(input())for _ in range(K)]
l,h=1,2**31
while l+1<h:
 m=(l+h)//2
 if sum(i//m for i in q)>=N:l=m
 else:h=m
print(l)