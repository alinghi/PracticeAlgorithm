def functor(n):
    def x(y):
        return (y+n-1)//n
    return x

a,b=map(int,input().split())
l=[0]*12
for _ in range(a):
    c,d=map(int,input().split())
    l[(d-1)*2+c]=l[(d-1)*2+c]+1
print(sum(map(functor(b),l)))