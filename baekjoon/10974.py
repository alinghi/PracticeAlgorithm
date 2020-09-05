import itertools
N=int(input())
for i in itertools.permutations(range(1,N+1),N):
    for j in i:
        print(j,end=" ")
    print()
