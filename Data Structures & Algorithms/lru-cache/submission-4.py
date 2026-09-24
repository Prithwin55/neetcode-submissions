class Node:
    def __init__(self,val,key,prev=None,next=None):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left=Node(0,0) #LRU
        self.right=Node(0,0) #MRU

        self.left.next=self.right
        self.right.prev=self.left

        self.cache={}

    def remove(self,node): #Removes node
        node.prev.next=node.next
        node.next.prev=node.prev
        # prev=node.prev
        # nxt=node.next
        # prev.next=nxt
        # nxt.prev=prev

    def insert(self,node): #Insert to MRU
        prev=self.right.prev
        nxt=self.right

        node.next=nxt
        node.prev=prev

        prev.next=node
        nxt.prev=node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(value,key)
        self.insert(node)
        self.cache[key]=node

        if len(self.cache) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
