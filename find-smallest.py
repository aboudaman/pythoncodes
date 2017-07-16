import time

t0 = time.time()
# Declare array to sort
arrToSort = [2323, 4,232,44,44, 2]

# Function to find smallest value
def findSmallest(array):
    # Assumes smallest value is first item
    smallest = array[0]
    index = 0
    # Loops through each item in the array starting at position 1
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            index = i
    return index
# Create Selection Sort Function
def selSort(arr):
    newSortedArray = []

    for val in range(len(arr)):
        smallVal = findSmallest(arr)
        newSortedArray.append(arr.pop(smallVal))
    return newSortedArray
t1 = time.time()
total = t0 + t1

# Output to the screen
print(selSort(arrToSort))

# Prints total time
print "Total Time:", total
