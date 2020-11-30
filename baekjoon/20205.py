N,K=map(int,input().split())
l=[]
for i in range(N):
    l.append(list(map(int,input().split())))
for row in l:
    for j in range(K):
        for col in row:
            for i in range(K):
                print(col,end=" ")
        print()
