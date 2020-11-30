import collections
S=input()
s=collections.Counter(S.upper())
z=s.most_common(2)
if len(z)==1:
    print(z[0][0])
elif z[0][1]==z[1][1]:
    print("?")
else:
    print(z[0][0])