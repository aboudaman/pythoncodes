from math import sqrt
mx = 10
pytha = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]

# Filter out those that are not integers
pytha = list(filter(lambda numb:numb[2].is_integer(), pytha))

#Outputs the result
print(pytha)
