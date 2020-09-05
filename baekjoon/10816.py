N=int(input())
l1=list(map(int,input().split()))
N=int(input())
l2=list(map(int,input().split()))
l1.sort()
def lower(elem,l=0,r=len(l1)-1):
	while l<=r:
		mid = (l + r) // 2
		if l1[mid]==elem:
			if mid==0 or l1[mid-1]!=elem:
				return mid
			else:
				return lower(elem,l,mid-1)
		elif l1[mid]<elem:
			l=mid+1
		else:
			r=mid-1
	return -1
def upper(elem,l=0,r=len(l1)-1):
	while l<=r:
		mid = (l + r) // 2
		if l1[mid]==elem:
			if mid==len(l1)-1 or l1[mid+1]!=elem:
				return mid
			else:
				return upper(elem,mid+1,r)
		elif l1[mid]<elem:
			l=mid+1
		else:
			r=mid-1
	return -1
for elem in l2:
	low=lower(elem)
	high=upper(elem)
	if low==-1 or high==-1:
		print(0,end=" ")
	else:
		print(high-low+1,end=" ")