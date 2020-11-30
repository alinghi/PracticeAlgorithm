l=list(map(int,input().split()))
l=[i*i for i in l]
print(sum(l)%10)