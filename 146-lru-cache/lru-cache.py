class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next,self.tail.prev=self.tail,self.head

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_to_front(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def get(self, key: int) -> int: 
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add_to_front(node)
            return node.value
        return -1    


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.remove(node)
            self.add_to_front(node)
        else:
            if len(self.cache)==self.capacity:
                del self.cache[self.tail.prev.key]
                self.remove(self.tail.prev)
            
            new=Node(key,value)
            self.add_to_front(new)
            self.cache[key]=new


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)