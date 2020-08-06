zero=[1,0,1,1]
zero.extend([-1]*40)
one=[0,1,1,2]
one.extend([-1]*40)
for i in range(4,42):
    zero[i]=zero[i-1]+zero[i-2]
    one[i] = one[i - 1] + one[i - 2]
def solution(n):
    print(zero[n],one[n])

N=int(input())
for _ in range(N):
    solution(int(input()))