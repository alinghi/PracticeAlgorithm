A,B,C=map(int,input().split())
x1,x2,y1,y2=map(int,input().split())

def functor(A,B,C):
    def ret(x):
        return A*x[0]+B*x[1]+C
    return ret

flag1=False
flag2=False
calc=functor(A,B,C)
l=[(x1,y1),(x1,y2),(x2,y1),(x2,y2)]
z=list(map(calc,l))
for i in z:
    if i>0:
        flag1=True
    elif i<0:
        flag2=True
if flag1 and flag2:
    print("Poor")
else:
    print("Lucky")