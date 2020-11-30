class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class SLL:
    #@contract
    #invariant: when contents exist self.current never never point HEADER!
    def __init__(self):
        self.head=Node("Head")
        self.tail=Node("Tail")
        self.current=self.head
        self.head.next=self.tail
        self.head.prev=self.tail
        self.tail.next=self.head
        self.tail.prev=self.head

    def add(self,data):
        x=Node(data)
        x.prev=self.current
        x.next=self.current.next
        self.current.next=x
        self.current=x
        x.next.prev=x

    def delete(self):
        if self.current==self.head:
            return
        else:
            self.current.prev.next=self.current.next
            self.current.next.prev=self.current.prev
            self.current=self.current.prev
    def p(self):
        ptr=self.head.next
        while ptr!=self.tail:
            print(ptr.data,end="")
            ptr=ptr.next
        print()
    def nn(self):
        if self.current.next==self.tail:
            return
        else:
            self.current=self.current.next
    def pp(self):
        if self.current==self.head:
            return
        else:
            self.current=self.current.prev
    def __repr__(self):
        s=""
        ptr = self.head.next
        while ptr != self.tail:
            s=s+ptr.data
            ptr = ptr.next
        s2 = ""
        ptr = self.tail.prev
        while ptr != self.head:
            s2 = s2 + ptr.data
            ptr = ptr.prev
        return s+"?"+s2

N=int(input())
for _ in range(N):
    z=SLL()
    s=input()
    cnt=0
    for ch in s:
        if ch=="<":
            z.pp()
        elif ch==">":
            z.nn()
        elif ch=="-":
            z.delete()
        else:
            z.add(ch)
        #print(cnt,str(z))
        cnt=cnt+1
    z.p()
