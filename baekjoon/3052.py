l=[]
for _ in range(10):
    l.append(int(input()))
s=set()
for i in l:
    s.add(i%42)
print(len(s))