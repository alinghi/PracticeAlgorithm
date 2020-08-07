l1=[]
l2=[]
for _ in range(3):
    l1.append(int(input()))
for _ in range(2):
    l2.append(int(input()))
print(min(l1)+min(l2)-50)