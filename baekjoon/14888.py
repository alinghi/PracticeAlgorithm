N=int(input())
l=list(map(int,input().split()))
plus,minus,mult,div=map(int,input().split())
MIN=9e9
MAX=-9e9

def calc(curr, i, plus,minus,mult,div):
    if i==N:
        global MIN, MAX
        MIN=min(MIN,curr)
        MAX = max(MAX, curr)
        return
    if plus:
        calc(curr+l[i],i+1,plus-1,minus,mult,div)
    if minus:
        calc(curr-l[i],i+1,plus,minus-1,mult,div)
    if mult:
        calc(curr*l[i],i+1,plus,minus,mult-1,div)
    if div:
        if curr<0:
            temp=-((-curr)//l[i])
        else:
            temp=curr//l[i]
        calc(temp,i+1,plus,minus,mult,div-1)
    return
calc(l[0],1,plus,minus,mult,div)
print(MAX)
print(MIN)