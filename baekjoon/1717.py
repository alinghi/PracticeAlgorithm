class UF:
    def __init__(self,n):
        self.id=[i for i in range(n+1)]
        self.sz=[1 for i in range(n+1)]
        self.count=n+1
    def count(self):
        return self.count
    def find(self,p):
        while (p!=self.id[p]):
            p=self.id[p]
        return p
    def connected(self,p,q):
        return self.find(p)==self.find(q)
    def union(self,p,q):
        i=self.find(p)
        j=self.find(q)
        if i==j:
            return
        if self.sz[i]<self.sz[j]:
            self.id[i]=j
            self.sz[j]=self.sz[j]+self.sz[i]
        else:
            self.id[j]=i
            self.sz[i] = self.sz[i] + self.sz[j]
        self.count=self.count-1

n,m=map(int,input().split())
uf=UF(n)
for _ in range(m):
    op,a,b=map(int,input().split())
    if op==0:
        uf.union(a,b)
    else:
        print("YES" if uf.connected(a,b) else "NO")

