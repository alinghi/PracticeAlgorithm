l1=list(map(int,input().split()))
l2=[1,1,2,2,2,8]
z=lambda x,y:x-y
l3=list(map(z,l2,l1))
for ch in l3:
    print(ch,end=" ")