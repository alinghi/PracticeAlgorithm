import itertools
N=int(input())
l,s=[1,5,10,50],set()
for i in itertools.combinations_with_replacement((0,1,2,3),N):
    coin=0
    for j in i: coin+=l[j]
    s.add(coin)
print(len(s))
