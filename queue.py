class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self._data = [None]* ArrayQueue.INITIAL_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def first(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        return self._data[self._front]
    
    def resizeArray(self, newSize):
        print("Resizing......")
        oldData = self._data
        self._data = [None] * newSize
        walk = self._front
        for i in range(self._size):
            self._data[i] = oldData[walk]
            walk = (walk + 1) % len(oldData)
        self._front = 0

    def enqueue(self,value):
        if self._size == len(self._data):
            self.resizeArray(2*len(self._data))
        available = (self._front+ self._size) % len(self._data)
        self._data[available] = value
        self._size = self._size + 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!!!")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._size = self._size - 1
        self._front = (self._front + 1)% len(self._data)
        return answer 
    
queue = ArrayQueue()

print("Queue Size >>",len(queue))
print("Is Empty ?", queue.isEmpty())
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(400)
queue.enqueue(500)
queue.enqueue(600)
queue.enqueue(700)
queue.enqueue(800)
queue.enqueue(900)
queue.enqueue(1000)
queue.enqueue(1100)
queue.enqueue(1200)
print("Queue Size >>",len(queue))
print("Is Empty ?", queue.isEmpty())

print("On Dequeue ", queue.dequeue())
print("On Dequeue ", queue.dequeue())
print("On Dequeue ", queue.dequeue())
print("On Dequeue ", queue.dequeue())

print("Queue Size >>",len(queue))
print("Is Empty ?", queue.isEmpty())
print("First Data ", queue.first())
    
    


