class _DoubleLinkedBase:
    
    class _Node:
        def __init__(self,e, prev, next):
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
        newNode = self._Node(e, predecessor, successor)
        predecessor._next = newNode
        successor._prev = newNode
        self._size += 1
        return newNode
    
    def delete(self, node):
        element = node._element
        predecessor  = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        return element
    
class PositionalList(_DoubleLinkedBase):
    
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            return type(self) == type(other) and self._node is other._node
        
        def __ne__(self, other):
            return not(self == other)
        
    def _validatePosition(self, position):
        if not isinstance(position, self.Position):
            raise Exception("This is not a valid position.")
        if position._container is not self:
            raise Exception("This position is not part of this list.")
        if position._node._next is None:
            raise Exception("Position is no longer valid.")
        
        return position._node
    
    def _createPosition(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self):
        return self._createPosition(self._header._next)
    
            
    def last(self):
        return self._createPosition(self._trailer._prev)
    
    def before(self, position):
        originalNode = self._validatePosition(position)
        return self._createPosition(originalNode._prev)
     
    def after(self, position):
        originalNode = self._validatePosition(position)
        return self._createPosition(originalNode._next)
    
    def __iter__(self):
        walk = self.first()
        while walk is not None:
            yield walk
            walk = self.after(walk)

    def insertBetween(self, e, predecessor, successor):
        newNode =  super().insertBetween(e, predecessor, successor)
        return self._createPosition(newNode)
    
    def addFirst(self,e):
        return self.insertBetween(e,self._header, self._header._next)
    
    def addLast(self,e):
        return self.insertBetween(e,self._trailer._prev, self._trailer)
    
    def addBefore(self,e, position):
        validNode = self._validatePosition(position)
        return self.insertBetween(e, validNode._prev, validNode)
    
    def addAfter(self,e, position):
        validNode = self._validatePosition(position)
        return self.insertBetween(e, validNode, validNode._next)
    
    def delete(self, position):
        validNode = self._validatePosition(position)
        return super().delete(validNode)
    
    def replace(self, e, position):
        validNode = self._validatePosition(position)
        oldElement = validNode._element
        validNode._element = e
        return oldElement

    

positions = PositionalList()
print("Size of position list is ", len(positions))  
print("List is empty ? ", positions.isEmpty())  
print("First position is ", positions.first())
print("Last position is ", positions.last())
positions.addFirst(100)
positions.addFirst(200)
positions.addLast(900)
positions.addLast(1000)

lastPosition = positions.last()
positions.replace(2222,lastPosition)

print("Size of position list is ", len(positions))  
print("List is empty ? ", positions.isEmpty())  
print("First position is ", positions.first().element())
print("Last position is ", positions.last().element())

allPositions = list(p.element() for p in positions)

print("All Positions ", allPositions)



class FavoriteList:

    class _Item:
        def __init__(self, e):
            self._value = e
            self._count = 0

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self)
    
    def _findPosition(self, e):
        current = self._data.first()
        while current is not None and current.element()._value != e:
            current = self._data.after(current)

        return current
    
    def _moveUp(self, position):
        if position != self._data.first():
            count = position.element()._count
            current = self._data.before(position)
            if count > current.element()._count:
                while current != self._data.first() and count > self._data.before(current).element()._count:
                    current = self._data.before(current)
                deletedElement = self._data.delete(position)
                self._data.addBefore(deletedElement, current)


    def access(self, e):
        position = self._findPosition(e)
        if position is None:
            position = self._data.addLast(self._Item(e))
        position.element()._count += 1
        self._moveUp(position)

    def remove(self, e):
        position = self._findPosition(e)
        if position is not None:
            self._data.delete(position)

    def top(self, k):
        if  not 1 <= k <= len(self):
            raise Exception("K is not in range!")
        current = self._data.first()
        for _i in range(k):
            item = current.element()
            yield item._value
            current = self._data.after(current)

myFavorites = FavoriteList()
print("Size of position list is ", len(myFavorites))  
print("List is empty ? ", myFavorites.isEmpty())  
print("First position is ", myFavorites.access('Hello World'))
print("First position is ", myFavorites.access('Big World'))

top1 = list(myFavorites.top(2))
print("Size of position list is ", len(myFavorites))  
print("List is empty ? ", myFavorites.isEmpty())  
print("Top Elements ", top1)

myFavorites.remove('Big World')
top2 = list(myFavorites.top(1))
print("Size of position list is ", len(myFavorites))  
print("List is empty ? ", myFavorites.isEmpty())  
print("Top Elements ", top2)

    

    
