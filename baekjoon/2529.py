import itertools
N=int(input())
s=list(input().split())
def determinant(s,cand):
    for i in range(len(s)):
        if s[i]=="<" and cand[i]>cand[i+1]:
            return False
        elif s[i]==">" and cand[i]<cand[i+1]:
            return False
    return True
MIN=(9,)*(N+1)
MAX=(0,)*(N+1)
for cand in itertools.permutations((0,1,2,3,4,5,6,7,8,9),N+1):
    if determinant(s,cand):
        MIN=min(MIN,cand)
        MAX = max(MAX, cand)
print("".join(map(str,MAX)))
print("".join(map(str,MIN)))