def shift(l, wise):
    if wise==1:
        return l[7:8]+l[:7]
    else:
        return l[1:]+l[0:1]
def score(l):
    return l[0][0]+2*l[1][0]+4*l[2][0]+8*l[3][0]
def check(l):
    b=[False, False, False]
    if l[0][2]!=l[1][6]:
        b[0]=True
    if l[1][2]!=l[2][6]:
        b[1]=True
    if l[2][2]!=l[3][6]:
        b[2]=True
    return b
def rotate(l,wheel_number,wise):
    wheel=wheel_number-1
    wi=wise
    i,j=wheel,wheel
    b=check(l)
    r=[0,0,0,0]
    r[wheel]=wi
    for k in range(1,4):
        wi=-wi
        if 0<=i-k<4:
            if b[i-k] and r[i-k+1]!=0:
                r[i-k]=wi
            else:
                r[i-k]=0
        if 0<=j+k<4:
            if b[j+k-1] and r[j+k-1]!=0:
                r[j+k]=wi
            else:
                r[j+k]=0
    for i in range(4):
        if r[i]!=0:
            l[i]=shift(l[i],r[i])
    return l

def init():
    l=[list(map(int,input())) for _ in range(4)]
    n=int(input())
    op=[list(map(int,input().split())) for _ in range(n)]
    return l,n,op

def solver(l,op):
    l2=l
    for i in op:
        l2=rotate(l2,i[0],i[1])
    return score(l2)

l,n,op=init()
print(solver(l,op))