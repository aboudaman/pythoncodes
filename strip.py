a = "  I AM"
# print (a.strip(' I'))
# print (a.strip().split(' '))
# print (b.strip().split(' '))
# print (a.split())
#
# print(" ".join())
a = (1, 3, 4, 5)

great = list(map(lambda x: x**2, a))

# great2 = list(map(lambda x, y: x=1 if x > y, a))
a = [1, 2]
b = [3, 3]
# tot = map(lambda a, b: a = 10 if a > b else 2, a, b)
# print tot(1,3)
# print tot
""" The code below will test the
map built in function in Python """

list_add = [2, 3, 4, 2]
list_add_second = [2, 3, 4, 1]
def add(x):
    return x + 1
map_res = map(add, list_add)

print (map_res)

def add_two_param(x = 1, y = 1):
    return x + y + 1

map_res_two = map(add_two_param, list_add, list_add_second)
print (map_res_two)
