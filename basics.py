greeting = "Hello World"
print(greeting)

class Node:
    def __init__(self,data):
        self._value = data
        self._next = None

class LinkedList:
    def __init__(self):
        self._size = 0
        self._head = None

    def size(self):
        return self._size

    def add(self, data):
        newNode = Node(data)
        if self._head:
            newNode._next = self._head
        self._head = newNode
        self._size += 1

    def getHead(self):
        return self._head._value


linkList = LinkedList()
print("List Size ", linkList.size())
linkList.add(100)
print("List head ", linkList.getHead())
print("List Size ", linkList.size())
linkList.add(200)
print("List head ", linkList.getHead())
print("List Size ", linkList.size())
linkList.add(300)
print("List head ", linkList.getHead())
print("List Size ", linkList.size())
linkList.add(400)
print("List head ", linkList.getHead())
print("List Size ", linkList.size())


class NumericProgression:

    def __init__(self,start=0):
        self._current = start

    def advance(self):
        self._current = self._current + 1

    def __next__(self):
        if self._current is None:
            raise Exception("No current found")
        answer = self._current
        self.advance()
        return answer
    
    def __iter__(self):
        return self

    def printProgression(self, number):
        progressString = ' '.join( str(next(self)) for i in range(number))
        print("Progression", progressString)


numProgress = NumericProgression()
numProgress.printProgression(5)


class ArithmeticProgression(NumericProgression):

    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._increment = increment

    def advance(self):
        self._current = self._current + self._increment

    
arithProgress1 = ArithmeticProgression()
arithProgress1.printProgression(5)

arithProgress2 = ArithmeticProgression(0,2)
arithProgress2.printProgression(5)

class GeometricProgression(NumericProgression):
    def __init__(self, start=1, base=1):
        super().__init__(start)
        self._base = base

    def advance(self):
        self._current = self._current * self._base

    
geoProgress1 = GeometricProgression()
geoProgress1.printProgression(10)

geoProgress2 = GeometricProgression(1,2)
geoProgress2.printProgression(10)


class FibonacciProgression(NumericProgression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def advance(self):
        self._prev, self._current = self._current, self._current + self._prev

    
fibProgress = FibonacciProgression()
fibProgress.printProgression(10)

fibProgress = FibonacciProgression(4,5)
fibProgress.printProgression(10)



def fibonacci(num):
    a = 0
    b = 1
    i = 0
    while i < num:
        yield a
        future = a + b
        a = b
        b = future
        i = i +1

myList = list(fibonacci(10))
print("My FIBONACCI list ", myList)

[a,b,c ]= [1,2,3]

print(a,b,c)


def findMax(arr):
    biggest = arr[0]
    for num in arr:
        if num > biggest:
            biggest = num
    
    return biggest
nums = [1244,44,21,5,65,9,123,43]
print("Largest in nums is ??", findMax(nums))

def binarySearchIterative(array, target, low, high):
    while low <= high:
        mid  = (high + low)// 2
        if target == array[mid]:
            return True
        elif target > array[mid]:
            low = mid + 1
        elif target < array[mid]:
            high = mid - 1
    return False

target1 = 222
target2= 123
target3 = 445
target4 = 47
target5 = 111
target6 = 3330
mySecondList = [223,445,476,555,644, 889,1999,2000,2100, 2300,3330]
print(f"List is ---> {mySecondList}.")
print(f"Target variable {target1} is present ?", binarySearchIterative(mySecondList,target1, 0, len(mySecondList)-1))
print(f"Target variable {target2} is present ?", binarySearchIterative(mySecondList,target2, 0, len(mySecondList)-1))
print(f"Target variable {target3} is present ?", binarySearchIterative(mySecondList,target3, 0, len(mySecondList)-1))
print(f"Target variable {target4} is present ?", binarySearchIterative(mySecondList,target4, 0, len(mySecondList)-1))
print(f"Target variable {target5} is present ?", binarySearchIterative(mySecondList,target5, 0, len(mySecondList)-1))
print(f"Target variable {target6} is present ?", binarySearchIterative(mySecondList,target6, 0, len(mySecondList)-1))


def reverseIteratively(arr, start, stop):
    while start < stop - 1:
        arr[start],arr[stop -1] = arr[stop - 1], arr[start]
        start,stop = start +1, stop -1 

print("BEFORE REVERSE \n", mySecondList)
reverseIteratively(mySecondList, 0, len(mySecondList))
print("AFTER REVERSE ''''''''''''''''''''''''''''''''''''''''''''''''\n", mySecondList)