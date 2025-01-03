class _DoubleLinkedBase:
    
    class _Node():
        def __init__(self, e,prev, next):
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
    
    def insertBetween(self, e, predecessor, successor):
        newNode = self._Node(e,predecessor, successor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1
        return newNode
    
    def delete(self, node):
        answer = node._element
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev =  predecessor
        self._size -= 1
        node._element = node._prev = node._next = None
        return answer
    

class PositionList(_DoubleLinkedBase):

    class Position:

        def __init__(self,container,node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node
        
        def __ne__(self, other):
            return not(self == other)
        

    def _validatePosition(self, position):
        if not isinstance(position, self.Position):
            raise Exception("It is not a valid Position")
        if position._container is not self:
            raise Exception("Position is not a part of this Position List")
        if position._node._next is None:
            raise Exception("Position is no longer valid")
        
        return position._node
    
    def _cratePosition(self,node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self):
        position = self._cratePosition(self._header._next)
        return position
    
    def last(self):
        position = self._cratePosition(self._trailer._prev)
        return position
    
    def after(self, position):
        node = self._validatePosition(position)
        return self._cratePosition(node._next)
    
    def before(self, position):
        node = self._validatePosition(position)
        return self._cratePosition(node._prev)
    
    def __iter__(self):
        current = self.first()
        while current is not None:
            yield current
            current = self.after(current)

    def insertBetween(self, e, predecessor, successor):
        node = super().insertBetween(e, predecessor, successor)
        return self._cratePosition(node)
    
    def addFirst(self,e):
        return self.insertBetween(e,self._header, self._header._next)
    
    def addLast(self,e):
        return self.insertBetween(e, self._trailer._prev, self._trailer)
    
    def addAfter(self,e, position):
        node = self._validatePosition(position)
        return self.insertBetween(e,node, node._next)
    
    def addBefore(self, e, position):
        node = self._validatePosition(position)
        return self.insertBetween(e,node._prev, node)
    
    def delete(self, position):
        node = self._validatePosition(position)
        return super().delete(node)
    
    def replace(self, e, position):
        node = self._validatePosition(position)
        oldValue = node._element
        node._element = e
        return oldValue
    

positions = PositionList()
print("Position list size ", len(positions))
print("Position list is empty!" if positions.isEmpty() else "Position list is NOT empty!")

print("First element", positions.first())
print("Last element", positions.last())

positions.addFirst(100)
positions.addFirst(200)
positions.addFirst(300)
positions.addFirst(400)
positions.addFirst(500)
positions.addLast(100)
positions.addLast(200)
positions.addLast(300)
positions.addLast(400)
positions.addLast(500)

print("Position list size ", len(positions))
print("Position list is empty!" if positions.isEmpty() else "Position list is NOT empty!")

print("First element", positions.first().element())
print("Last element", positions.last().element())

allPositions = list( position.element() for  position in positions)
print("Position List elements ", allPositions)

firstPosition = positions.first()
newFirstPosition = positions.addBefore(9999, firstPosition)
secondPosition = positions.addAfter(0.001, newFirstPosition)
deletedElement = positions.delete(secondPosition)

print("Deleted position ", deletedElement)
positions.replace(2025, newFirstPosition)

allPositions = list( position.element() for  position in positions)
print("Position List elements ", allPositions)


def positionInsertionSort(list):
    marker = list.first()
    
    while marker != list.last():
        pivot =  list.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = list.after(pivot)
        else:
            walk = marker
            while walk != list.first() and list.before(walk).element() > value:
                walk = list.before(walk)
            list.delete(pivot)
            list.addBefore(value, walk)

positionInsertionSort(positions)

afterSort = list( position.element() for  position in positions)
print("Position List elements After sort >>", afterSort)



        
        
        
