class _DoubleLikedBase:

    class _Node():
        def __init__(self,e,prev,next):
            self._element = e
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return len(self) == 0
    
    def insertBetween(self,e,predecessor, successor):
        newNode = self._Node(e,predecessor,successor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1

        return newNode
    
    def deleteNode(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._element = node._prev = node._next = None
        self._size -= 1
        return element
    

class DoublyLinkedDeque(_DoubleLikedBase):

    def first(self):
        if self.isEmpty():
            raise Exception("List is empty!")
        return self._header._next._element
    
    def last(self):
        if self.isEmpty():
            raise Exception("List is empty!")
        return self._trailer._prev._element
    
    def insertFirst(self,e):
        self.insertBetween(e, self._header, self._header._next)
    
    def insertLast(self,e):
        self.insertBetween(e, self._trailer._prev, self._trailer)

    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("Deque is Empty!")
        self.deleteNode(self._header._next)

    def deleteLast(self):
        if self.isEmpty():
            raise Exception("Deque is Empty!")
        self.deleteNode(self._trailer._prev)
    
deque = DoublyLinkedDeque()

print("Deque Size >>",len(deque))
print("Is Empty ?", deque.isEmpty())

deque.insertFirst(10000)
deque.insertFirst(99990000)
deque.insertLast(20000)

print("First element is ", deque.first())
print("First element is ", deque.last())

print("Deque Size >>",len(deque))
print("Is Empty ?", deque.isEmpty())
    
