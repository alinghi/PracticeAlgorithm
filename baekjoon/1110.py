def solution(N):
    ten,one=N//10,N%10
    s=ten+one
    sten,sone=s//10,s%10
    return 10*one+sone

N=int(input())
ret=solution(N)
i=1
while ret!=N:
    ret=solution(ret)
    i+=1
print(i)