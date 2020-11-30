import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Sentinel(Node):
    def __init__(self,data):
        Node.__init__(self,data)
        self.number=0
class Queue:
    def __init__(self):
        self.head=Sentinel("HEAD")
        self.tail=Sentinel("TAIL")
        self.head.next=self.tail
        self.head.prev=self.tail
        self.tail.next=self.head
        self.tail.prev=self.head
    def push(self,x):
        Z=Node(x)
        self.head.number+=1
        Z.prev=self.tail.prev
        Z.next=self.tail
        self.tail.prev.next=Z
        self.tail.prev=Z
    def pop(self):
        if self.head.number==0:
            print(-1)
        else:
            print(self.head.next.data)
            self.head.next.next.prev=self.head
            self.head.next=self.head.next.next
            self.head.number-=1
    def front(self):
        if self.head.number==0:
            print(-1)
        else:
            print(self.head.next.data)
    def back(self):
        if self.head.number==0:
            print(-1)
        else:
            print(self.tail.prev.data)


q=Queue()
N=int(input())
for _ in range(N):
    s=sys.stdin.readline().split()
    if s[0]=="push":
        q.push(int(s[1]))
    elif s[0]=="pop":
        q.pop()
    elif s[0]=="front":
        q.front()
    elif s[0]=="back":
        q.back()
    elif s[0]=="size":
        print(q.head.number)
    elif s[0]=="empty":
        print(1 if q.head.number==0 else 0)
