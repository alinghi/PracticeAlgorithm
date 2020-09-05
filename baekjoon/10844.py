N=int(input())
l=[[1],[0,2],[1,3],[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8]]
init=[0,1,1,1,1,1,1,1,1,1]
temp=[0,0,0,0,0,0,0,0,0,0]
p=1000000000
for i in range(1,N):
    for j in range(10):
        temp[j]=0
        for ll in l[j]:
            temp[j]+=init[ll]
    for j in range(10):
        init[j]=temp[j]%p
print(sum(init)%p)