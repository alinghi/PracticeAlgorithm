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
            return
        else:
            ret=self.head.next.data
            self.head.next.next.prev=self.head
            self.head.next=self.head.next.next
            self.head.number-=1
            return ret
    def front(self):
        if self.head.number==0:
            return
        else:
            print(self.head.next.data)


q=Queue()
N=int(input())
for i in range(1,N+1):
    q.push(i)
while q.head.number!=1:
    q.pop()
    q.push(q.pop())
q.front()