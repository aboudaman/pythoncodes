arr = [2323, 4,232,44,44, 2]

# Function to find smallest value
def findSmallest(array):
    # Assumes smallest value is first item
    smallest = array[0]
    # Loops through each item in the array starting at position 1
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest

# output result to the screen
print(findSmallest(arr))
