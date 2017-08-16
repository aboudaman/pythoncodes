import sys
# print("What is your name")
# name = input()
# print("How old are you")
# age = input("How old are you => ")
#
# print(f"Hello {name}, welcome to virtual world, so, you are {age} " \
#     "years old")
li = [2, 4, 4, 6, 6, 6]

# print(li.count(max(li)))
name_space = "I AM ME"
# name_join = ' '.join(name_space[1:])

# print(name_space)
# print(name_join)
# print(len(sys.argv))
# print(sys.argv)
# print(' '.join(sys.argv[1:]))
# time = '12:03:45'
# print(time[0:2])
l1 = [10, 2, 2, 4, 5]
l2 = [1, 20, 2, 4, 5]
lot_length = 11
# a = []
# print("Enter values for A")
def lotprob(lot_length, letter):
    print(f"Enter Value for {letter}")
    num_list = []
    for i in range(1, lot_length):
        # print("Enter val for A")
        while True:
            input_val = input(f"{i} value: ")
            if input_val.isdigit():
                num_list.append(input_val)
                break
            else:
                print("A number is required")
    return num_list





# l3 = l1 + l2
# seen = set()
# for num in l3:
#     if num not in seen:
#         print(f"{num} occurs {l3.count(num)} times")
        # seen.add(num)
a = lotprob(11, 'A')
b = lotprob(11, 'B')
c = lotprob(11, 'C')
print(f"List is {a}")
print(a[1])
print(f"List is {b}")
print(b[1])
