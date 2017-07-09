arr = [2323, 4,232,44,44, 2]

def findSmallest(array):
    smallest = array[0]
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest

print(findSmallest(arr))
