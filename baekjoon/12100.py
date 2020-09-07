import copy
import itertools
import sys
#sys.stdin=open("input.txt","r")
#sys.stdout=open("output.txt","w")

def traverse(row, col, dRow, dCol, l):
    n,ret=len(l),[]
    count=0
    while count<n:
        if l[row][col]!=0:
            ret.append(l[row][col])
            l[row][col]=0
        row, col, count = row+dRow, col+dCol, count + 1
    return ret

def gravityElement(row, col, dRow, dCol, l, tra):
    while tra:
        x=tra.pop()
        if l[row][col]==0:
            l[row][col]=x
        elif l[row][col]==x:
            l[row][col]=2*x
            row, col = row + dRow, col + dCol
        else:
            row, col = row + dRow, col + dCol
            l[row][col] = x

def gravity(l,direction):
    n=len(l)
    #up 0 right 1 down 2 left 3
    for i in range(len(l)):
        if direction==0:
            gravityElement(0,i,1,0,l,traverse(n-1,i,-1,0,l))
        elif direction==1:
            gravityElement(i,n-1,0,-1,l,traverse(i,0,0,1,l))
        elif direction==2:
            gravityElement(n-1,i,-1,0,l,traverse(0,i,1,0,l))
        else:
            gravityElement(i,0,0,1,l,traverse(i,n-1,0,-1,l))

def _2048(l,op):
    aList=copy.deepcopy(l)
    for i in op:
        gravity(aList,i)
    ans=0
    for i in range(len(l)):
        ans=max(ans,max(aList[i]))
    return ans

def init(n):
    l=[list(map(int,input().split())) for _ in range(n)]
    return l

def solver():
    n=int(input())
    l=init(n)
    ans=0
    for op in itertools.product(range(4),repeat=5):
        ans=max(ans,_2048(l,op))
    print(ans)
    return



solver()