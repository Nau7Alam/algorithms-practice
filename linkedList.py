class LinkedStack:

    class _Node:
        __slots__ = '_element','_next'
        def __init__(self,e, next):
            self._element = e
            self._next = next
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return len(self) == 0
    
    def top(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!!")
        return self._head._element
    
    def push(self, e):
        newNode = self._Node(e,self._head)
        self._head = newNode
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    

stack = LinkedStack()

print("Linked Stack size is >>>> ", len(stack))
print("Stack is empty ?? ", stack.isEmpty())

stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
stack.push(500)
stack.push(600)

print("Linked Stack size is >>>> ", len(stack))
print("Stack is empty ?? ", stack.isEmpty())
print("ON POP ", stack.pop())
stack.push(1000)
print("Current Top is ", stack.top())
print('\n-------------------------------------------\n')


class LinkedQueue:

    class _Node:
        def __init__(self,e,next):
           self._element = e
           self._next = next 

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return len(self) == 0
    
    def first(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        return self._head._element
    
    def last(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        return self._tail._element
    
    def enqueue(self, e):
        newNode = self._Node(e,None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        answer = self._head._element
        self._size -=1
        self._head = self._head._next
        if self.isEmpty():
            self._tail = None
        return answer

linkedQueue = LinkedQueue()

print("Linked Queue size is >>>> ", len(linkedQueue))
print("Queue is empty ?? ", linkedQueue.isEmpty())

linkedQueue.enqueue(1000)
linkedQueue.enqueue(2000)
linkedQueue.enqueue(3000)
linkedQueue.enqueue(4000)
linkedQueue.enqueue(5000)

print("Linked Queue size is >>>> ", len(linkedQueue))
print("Queue is empty ?? ", linkedQueue.isEmpty())
print("First in the queue is >>>> ", linkedQueue.first())
print("First in the queue is >>>> ", linkedQueue.last())
print("ON dequeue ",linkedQueue.dequeue())
print("ON dequeue ",linkedQueue.dequeue())
print("ON dequeue ",linkedQueue.dequeue())
print("Linked Queue size is >>>> ", len(linkedQueue))
print("Queue is empty ?? ", linkedQueue.isEmpty())
print("First in the queue is >>>> ", linkedQueue.first())
print("First in the queue is >>>> ", linkedQueue.last())

print('\n-------------------------------------------\n')


class CircularQueue:

    class _Node:
        def __init__(self,e , next):
            self._element = e
            self._next = next
    
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def first(self):
        if self.isEmpty():
            raise Exception("Circular Queue is empty!")
        return self._tail._next._element

    def last(self):
        if self.isEmpty():
            raise Exception("Circular Queue is empty!")
        return self._tail._element

    def enqueue(self,e):
        newNode = self._Node(e, None)
        if self.isEmpty():
            newNode._next = newNode
        else:
            newNode._next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Circular Queue is empty!")
        oldHead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldHead._next
        self._size -= 1
        return oldHead._element


circularQueue = CircularQueue()

print("Linked Queue size is >>>> ", len(circularQueue))
print("Queue is empty ?? ", circularQueue.isEmpty())

circularQueue.enqueue(1000)
circularQueue.enqueue(2000)
circularQueue.enqueue(3000)
circularQueue.enqueue(4000)
circularQueue.enqueue(5000)

print("Circular Queue size is >>>> ", len(circularQueue))
print("Queue is empty ?? ", circularQueue.isEmpty())
print("First in the queue is >>>> ", circularQueue.first())
print("First in the queue is >>>> ", circularQueue.last())
print("ON dequeue ",circularQueue.dequeue())
print("ON dequeue ",circularQueue.dequeue())
print("ON dequeue ",circularQueue.dequeue())
print("Linked Queue size is >>>> ", len(circularQueue))
print("Queue is empty ?? ", circularQueue.isEmpty())
print("First in the queue is >>>> ", linkedQueue.first())
print("First in the queue is >>>> ", circularQueue.last())

print('\n-------------------------------------------\n')