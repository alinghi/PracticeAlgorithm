N=int(input())
l1=list(map(int, input().split()))
N=int(input())
l2=list(map(int, input().split()))
l1.sort()
def finded(elem) :
    low=0
    high=len(l1)-1
    while low<=high:
        mid = (low + high) // 2
        if l1[mid]==elem:
            return 1
            elif l1[mid]<elem:
            low=mid+1
        else:
high=mid-1
return 0
for elem in l2:
print(finded(elem), end=" ")
