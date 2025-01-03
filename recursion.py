import os;
import sys;

def factorial(num):
    if num == 0:
        return 1
    
    return num * factorial(num -1)

print("Factorial of 3 is ", factorial(3))
print("Factorial of 12 is ", factorial(12))
print("Factorial of 99 is ", factorial(99))

print('\n\n')


def drawLine(numberOfLine, value=''):
    line =  '-' * numberOfLine
    if value:
        line = line + ' ' + value
    print(line)

def printInterval(interval):
    if(interval > 0):
        printInterval(interval - 1)
        drawLine(interval)
        printInterval(interval - 1)

def printScale(length,maxInterval):
    drawLine(maxInterval,'0')
    for value in range(1,length+1):
        printInterval(maxInterval - 1)
        drawLine(maxInterval,str(value))


printScale(1,5)
print('\n\n')
printScale(2,4)


print('\n\n')

def binarySearch(sortedArr, target, low, high):
    if low > high:
        return False
    mid = (high+low)//2
    if target == sortedArr[mid]:
        return True
    elif target > sortedArr[mid]:
        return binarySearch(sortedArr, target, mid + 1, high)
    elif target < sortedArr[mid]:
        return binarySearch(sortedArr, target, low, mid - 1)
    
    return False

target1 = 12
target2= 11
target3 = 45
target4 = 47
target5 = 111
target6 = 99

myList = [1,3,8,11,12,15,33,45,55,65,77,78,89,99,104]

print(f"Target variable {target1} is present ?", binarySearch(myList,target1, 0, len(myList)-1))
print(f"Target variable {target2} is present ?", binarySearch(myList,target2, 0, len(myList)-1))
print(f"Target variable {target3} is present ?", binarySearch(myList,target3, 0, len(myList)-1))
print(f"Target variable {target4} is present ?", binarySearch(myList,target4, 0, len(myList)-1))
print(f"Target variable {target5} is present ?", binarySearch(myList,target5, 0, len(myList)-1))
print(f"Target variable {target6} is present ?", binarySearch(myList,target6, 0, len(myList)-1))

print('\n------------------------------------\n')

target1 = 222
target2= 123
target3 = 445
target4 = 47
target5 = 111
target6 = 3330
mySecondList = [223,445,476,555,644, 889,1999,2000,2100, 2300,3330]
print(f"Target variable {target1} is present ?", binarySearch(mySecondList,target1, 0, len(mySecondList)-1))
print(f"Target variable {target2} is present ?", binarySearch(mySecondList,target2, 0, len(mySecondList)-1))
print(f"Target variable {target3} is present ?", binarySearch(mySecondList,target3, 0, len(mySecondList)-1))
print(f"Target variable {target4} is present ?", binarySearch(mySecondList,target4, 0, len(mySecondList)-1))
print(f"Target variable {target5} is present ?", binarySearch(mySecondList,target5, 0, len(mySecondList)-1))
print(f"Target variable {target6} is present ?", binarySearch(mySecondList,target6, 0, len(mySecondList)-1))


print('\n ------------- Recursion in file directory structure ------------- \n')
def calculateFolderSize(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            childPath = os.path.join(path, file)
            total = total + calculateFolderSize(childPath)

    return total

basicsFile = os.path.join(os.getcwd(), 'basics.py')
print(f"File size of {basicsFile} in byte is >>", calculateFolderSize(basicsFile))
algoFolder = '/Users/naushadalam/Developer/python/algo'
print(f"File size of {algoFolder} folder in byte is >>", calculateFolderSize(algoFolder))
developerFolder = '/Users/naushadalam/Developer/TypeScript'
print(f"File size of {developerFolder} folder in byte is >>", calculateFolderSize(developerFolder))

print('\n\n')

# Code with infinite recursion
# def callMe(n):
#     callMe(n)

# callMe(100)

# print("BEFORE ",sys.getrecursionlimit())
# sys.setrecursionlimit(111)
# print("AFTER ",sys.getrecursionlimit())

def linearSum(arr, addNElements):
    if addNElements < 1:
        return 0

    return arr[addNElements - 1] + linearSum(arr, addNElements -1)

sumNumbers = [200,12,2,1,1,20, 100, 300]
print(f"Sum of first {2} is ", linearSum(sumNumbers,2))
print(f"Sum of first {4} is ", linearSum(sumNumbers,4))
print(f"Sum of first {5} is ", linearSum(sumNumbers,5))
print(f"Sum of first {len(sumNumbers)} is ", linearSum(sumNumbers,len(sumNumbers)))


def reverseArray(S, start, stop):
    if start < stop - 1:
        S[start],S[stop - 1] = S[stop - 1],S[start]
        start,stop = start + 1, stop - 1
        reverseArray(S,start,stop)

print("BEFORE REVERSE \n", sumNumbers)
reverseArray(sumNumbers, 0, len(sumNumbers))
print("AFTER REVERSE \n", sumNumbers)

def powerOf(number, power):
    if power == 0:
        return 1
    else:
        return number * powerOf(number, power -1)

print('2 power 3 is ',powerOf(2,3))
print('6 power 3 is ',powerOf(6,2))
print('100 power 1 is ',powerOf(100,1))

print("\n")


def binarySum(array, start, stop):
    if start >= stop:
        return 0
    elif start == stop -1:
        return array[start]
    else:
        mid = (start+ stop)//2
        return binarySum(array , start, mid) + binarySum(array, mid, stop)

print("BINARY SUM \n", binarySum(mySecondList, 0, len(mySecondList)))