l=[]
for _ in range(5):
    x=int(input())
    if x<40:
        l.append(40)
    else:
        l.append(x)
print(sum(l)//5)