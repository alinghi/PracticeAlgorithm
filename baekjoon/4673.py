N=10001
def d(n):
    ret=n
    while True:
        if n==0: break
        ret+=n%10
        n=n//10
    return ret

ans=[True]*10001
ans[0]=False
for i in range(N):
    tmp=d(i)
    if tmp<10001:
        ans[d(i)]=False
for i in range(N):
    if ans[i]:print(i)