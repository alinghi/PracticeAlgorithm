N,r,c=map(int,input().split())
pow=lambda x:2**x
def calc(N,r,c):
    if N==1:
        return 2*r+c
    temp=pow(N)//2
    R=1 if r>=temp else 0
    C=1 if c>=temp else 0
    return calc(N-1,r-temp*R,c-temp*C)+(2*R+C)*(temp*temp)
print(calc(N,r,c))