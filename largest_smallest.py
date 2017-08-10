import heapq
from collections import Counter

nums = [1, 8, 2, 23, 7, -4, 18, 23, 43, 43, 2]

# print(heapq.nlargest(1, nums))

# Assume first iteem is the largest
high = nums[0]
for n in range(1, len(nums)):
    # print(n)
    if nums[n] > high:
        high = nums[n]
        # freq = count()

print(high)
# Check is the number has other occurences
counts = Counter(nums)
print(high in counts)
print(counts[high])
# print(counts)
