a = [12, 20, 22, 33, 44, 122, 200, 442, 4522, 55223, 55322]

# Algorithm to to perform a binary search on a sorted list
def binSearch(item, val):
    low = 0
    high = len(item) - 1
    while (low <= high):
        mid =  (low + high) // 2
        if (item[mid] > val):
            high = mid - 1
        elif (item[mid] < val):
            low = mid + 1
        else:
            return "Found"
    return "Not Found"
