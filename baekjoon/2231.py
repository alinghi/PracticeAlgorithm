x=lambda z:z+sum(map(int,list(str(z))))
def solution(N):
    i = 1
    while i<=N:
        if x(i)==N:
            return i
        i+=1
    return 0
print(solution(int(input())))