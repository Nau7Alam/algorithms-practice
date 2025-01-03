def insertionSort(S):
    for i in range(1,len(S)):
        curr = S[i]
        j = i
        while j > 0 and S[j -1] > curr:
            S[j] = S[j -1]
            j = j - 1
        S[j] = curr

listToSort = [23,73,56,1,45,91,34,220,19,44]
print("Unsorted List >>>> ", listToSort)
insertionSort(listToSort)
print("Sorted List ==== ", listToSort)
