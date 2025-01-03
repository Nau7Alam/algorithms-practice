class LinkedQueue:
    class _Node:
        def __init__(self,e, next):
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
    
    def head(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        return self._head._element
    
    def tail(self):
        if self.isEmpty():
            raise Exception("Queue is Empty!")
        return self._tail._element
    
    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        oldHead = self._head
        element = oldHead._element
        self._head = oldHead._next
        self._size -= 1
        if self.isEmpty():
            self._tail = None
        return element
  

class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("Should be implemented by Sub-class")
        
        def __eq__(self, other):
            raise NotImplementedError("Should be implemented by Sub-class")
        
        def __ne__(self, other):
            return not(self == other)

    def root(self):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def isRoot(self, p):
        return self.root() == p
    
    def children(self,p):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def parent(self,p):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def numChildren(self, p):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def isLeaf(self, p):
        return self.numChildren(p) == 0
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        raise NotImplementedError("Should be implemented by Sub-class")

    def subTreePreOrderTraversal(self,p):
        yield p
        for child in self.children(p):
            for other in self.subTreePreOrderTraversal(child):
                yield other
    
    def preOrderTraversal(self):
        if not self.isEmpty():
            for p in self.subTreePreOrderTraversal(self.root()):
                yield p

    def subTreePostOrderTraversal(self,p):
        for child in self.children(p):
            for other in self.subTreePostOrderTraversal(child):
                yield other
        yield p

    def postOrderTraversal(self):
        if not self.isEmpty():
            for position in self.subTreePostOrderTraversal(self.root()):
                yield position

    def positions(self):
        return self.preOrderTraversal()

    def __iter__(self):
        for position in self.positions():
            yield position.element()

    def depthFirstTraversal(self):
        if not self.isEmpty():
            Queue = LinkedQueue()
            Queue.enqueue(self.root())
            while not Queue.isEmpty():
                position = Queue.dequeue()
                yield position
                for child in self.children(position):
                    Queue.enqueue(child)
    

class BinaryTree(Tree):
    def left(self,p):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def right(self,p):
        raise NotImplementedError("Should be implemented by Sub-class")
    
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def sibling(self, p):
        parent  = self.parent(p)
        if parent is None:
            return None
        else:
            if p is self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def subTreeInOrderTraversal(self,p):
        if self.left(p) is not None:
            for other in self.subTreeInOrderTraversal(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self.subTreeInOrderTraversal(self.right(p)):
                yield other

    def inOrderTraversal(self):
        if not self.isEmpty():
            for position in self.subTreeInOrderTraversal(self.root()):
                yield position
            
    def positions(self):
        return self.inOrderTraversal()
    
    def __iter__(self):
        for position in self.positions():
            yield position.element()
    

class LinkedBinaryTree(BinaryTree):
    class _Node:
        def __init__(self,e, parent= None, left= None, right= None):
            self._element = e
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self,container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            return type(self) is type(other) and self._node is other._node
        

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def _validatePosition(self,position):
        if not isinstance(position, self.Position):
            raise Exception("Not a valid Position!")
        if self is not position._container:
            raise Exception("Not a part of this Binary Tree!")
        if position._node._parent is position._node:
            raise Exception('Position is no longer valid!')
        
        return position._node
    
    def _makePosition(self, node):
        return self.Position(self,node) if node is not None else None

    def root(self):
        return self._makePosition(self._root)
    
    def parent(self, p):
        node = self._validatePosition(p)
        return self._makePosition(node._parent)
    
    def right(self, p):
        node = self._validatePosition(p)
        return self._makePosition(node._right)
    
    def left(self, p):
        node = self._validatePosition(p)
        return self._makePosition(node._left)
    
    def numChildren(self,p):
        node = self._validatePosition(p)
        count = 0
        if node._left is not None:
            count+= 1
        if node._right is not None:
            count+= 1
        return count

    def addRoot(self, e):
        if self._root is not None:
            raise ValueError("Root is already present!")
        self._root = self._Node(e)
        self._size = 1
        return self._makePosition(self._root)
    
    def addLeft(self,p,e):
        node = self._validatePosition(p)
        if node._left is not None:
            raise ValueError("Left is already present!")
        node._left = self._Node(e)
        self._size += 1
        return self._makePosition(node._left)
    
    def addRight(self, p, e):
        node = self._validatePosition(p)
        if node._right is not None:
            raise ValueError("Right is already present!")
        node._right = self._Node(e)
        self._size += 1
        return self._makePosition(node._right)
    
    def replace(self, p, e):
        node = self._validatePosition(p)
        oldValue = node._element
        node._element = e
        return oldValue
    
    def delete(self, p):
        if self.numChildren(p) == 2:
            raise ValueError("p already has two children!")
        node = self._validatePosition(p)
        child = node._left if node._left else node._right
        if node is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    
    def attach(self, p, t1, t2):
        node = self._validatePosition(p)
        if not self.isLeaf(p):
            raise ValueError("Position should be a leaf i.e no children!")
        if not type(self) is type(t1) is type(t2):
            raise ValueError("Tree 1 and Tree 2 should be of type Tree!")
        self._size += len(t1) + len(t2)
        if not t1.isEmpty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.isEmpty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def depth(self, p):
        if self.isRoot(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height2(self,p):
        if self.isLeaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self,p = None):
        if p is None:
            p = self.root()
        return self._height2(p)



T = LinkedBinaryTree()
print("Size of tree is ", len(T))
print("Tree is empty ??", T.isEmpty())
root = T.addRoot(100)
left = T.addLeft(root, 200)
leftLeft = T.addLeft(left, 400)
leftRight = T.addRight(left, 500)
right = T.addRight(root, 300)
rightLeft = T.addLeft(right, 600)
rightRight = T.addRight(right, 700)
print("Size of tree is ", len(T))
print("Tree is empty ??", T.isEmpty())

inOrderElements = list(T)
print("inOrderElements", inOrderElements)
preOrderElements = [position.element() for position in T.preOrderTraversal()]
print("preOrderElements", preOrderElements)
postOrderElements = [position.element() for position in T.postOrderTraversal()]
print("postOrderElements", postOrderElements)
depthFirstElements = [position.element() for position in T.depthFirstTraversal()]
print("depthFirstElements", depthFirstElements)
    
    


        

    
    

              