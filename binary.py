#This program converts a number n to binary
n = 40
remainders = []

while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)

print (remainders[::-1])
