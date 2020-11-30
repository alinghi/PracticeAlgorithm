N=int(input())
l=[tuple(map(int,input().split())) for _ in range(N)]
rank=[]
for idx1,i in enumerate(l):
    cnt_i=0
    for idx2,j in enumerate(l):
        if idx1==idx2:
            continue
        if i[0]<j[0] and i[1]<j[1]:
            cnt_i+=1
    print(cnt_i+1,end=" ")