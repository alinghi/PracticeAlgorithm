class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.higher={i:[] for i in range(1000)}

    def add(self, key: int) -> None:
        high,low=self.div(key)
        if self.contains(key):
            return
        self.higher[high].append(low)
        

    def remove(self, key: int) -> None:
        high,low=self.div(key)
        if not self.contains(key):
            return
        self.higher[high].remove(low)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        high,low=self.div(key)
        if low in self.higher[high]:
            return True
        else:
            return False
    def div(self,key:int):
        return key//1000, key%1000
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)