l=[i for i in range(1,21)]
for _ in range(10):
    a,b=map(int,input().split())
    for i in range((b-a+1)//2):
        l[a-1+i],l[b-1-i]=l[b-1-i],l[a-1+i]
for i in l:
    print(i,end=" ")