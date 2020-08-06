a,b,c=map(int,input().split())
if b>=c:
    print(-1)
else:
    x=a//(c-b)
    print(x+1)