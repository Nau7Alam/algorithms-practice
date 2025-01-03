import os;

class Stack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self) == 0
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.data[-1]

stack = Stack()
print("Stack Size >>",len(stack))
print("Is Empty ?", stack.isEmpty())
stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)
print("Stack Size >>",len(stack))
print("Is Empty ?", stack.isEmpty())
print("Stack top ", stack.top())
stack.pop()
stack.push(1100)
stack.push(2200)
stack.pop()
stack.pop()
print("Stack Size >>",len(stack))
print("Is Empty ?", stack.isEmpty())
print("Stack top ", stack.top())


def reverseFileContent(path):
    readLines = open(path)
    lineStack = Stack()
    for line in readLines:
        lineStack.push(line)
    readLines.close()

    writeLines = open(path,'w')
    while not lineStack.isEmpty():
        line = lineStack.pop()
        writeLines.write(line)
    writeLines.close()

# storyFile = os.path.join(os.getcwd(),'story.txt')
# print("Reading from ",storyFile)
# reverseFileContent(storyFile)

print('\n')

def checkMatchingBrackets(equation):
    openBrackets = '{(['
    closeBrackets = '})]'
    openBracketStack = Stack()

    for character in equation:
        if character in openBrackets:
            openBracketStack.push(character)
        elif character in closeBrackets:
            if openBracketStack.isEmpty():
                return False
            elif closeBrackets.index(character) != openBrackets.index(openBracketStack.pop()):
                return False
    return openBracketStack.isEmpty()

validEquation1 = '([12+1]+12(23+12)*{12+12})'
print(validEquation1 ,"is a valid equation? ",checkMatchingBrackets(validEquation1))
validEquation2 = '{12+1(12-55+[567*23])}'
print(validEquation2 ,"is a valid equation? ",checkMatchingBrackets(validEquation2))
validEquation3 = '([12+1]+12(23+12)*{12+12)'
print(validEquation3 ,"is a valid equation? ",checkMatchingBrackets(validEquation3))
validEquation4 = '([{}}}'
print(validEquation4 ,"is a valid equation? ",checkMatchingBrackets(validEquation4))


def isValidHTML(htmlString=''):
    tagStack = Stack()
    j = htmlString.find('<')
    while j != -1:
        k = htmlString.find('>', j + 1)
        if k == -1:
            return False
        tag = htmlString[j+1: k]
        if not tag.startswith('/'):
            tagStack.push(tag)
        else:
            if tagStack.isEmpty():
                return False
            elif tag[1:] != tagStack.pop():
                return False
        j = htmlString.find('<',k+1)
    return tagStack.isEmpty()

htmlString ='<html><head>Hello World</head><body><h1>This is an html heading</h1></body></html>'
print(htmlString, " is a valid HTML ", isValidHTML(htmlString))

htmlString2 ='<html><head>Hello World</head><body><h1>This is an html heading <body></html>'
print(htmlString2, " is a valid HTML " if isValidHTML(htmlString2) else "Not a Valid HTML")

