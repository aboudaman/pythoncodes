""" String Operations in Python """
name = "%  abacdd2^    ** %% ##%"
# print (name)
# print (name.lstrip('%'))

name2 = "We are magic in Orlando"

list_num = [2, 4, 5, 3, 0]
space = 'X' * 5

# print(round(len([x for x in list_num if x > 2])/3, 2))

# print (space.rjust(5, ' '))

n = 6
symb = '#'
temp_n = n
for symbol in range(1, n+1):
        temp_symbol = symb * symbol
        # print (temp_symbol.rjust(n, ' '))

emp_profile = ('name', 'address', 'sex', 'tel', 'ssn', 'emergency_contact')
*info, cont = emp_profile

print (info)
print (cont)
print(info[1])
