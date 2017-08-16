def lotprob(lot_length, letter):
    print(f"Enter Value for {letter}")
    num_list = []
    for i in range(1, lot_length + 1):
        # print("Enter val for A")
        while True:
            input_val = input(f"{i} value: ")
            if input_val.isdigit():
                num_list.append(input_val)
                break
            else:
                print("A number is required")
    return num_list
alist = [20, 24, 26, 35, 49]
blist = [12, 30, 36, 47,62]
clist = [11, 21, 28, 33, 45, 11]
dlist = [1, 16, 54, 63, 69, 18]
elist = [1, 28, 40, 45, 48, 12]
flist = [7, 19, 21, 42, 69, 12]
glist = [5, 32, 44, 53, 60, 9]
hlist = [50, 51, 59, 61, 63, 4]
ilist = [9, 40, 63, 64, 66, 17]
jlist = [1, 2, 18, 23, 61, 9]

# a = lotprob(6, 'A')
# b = lotprob(6, 'B')
# c = lotprob(6, 'C')
comp_list = alist + blist + clist + dlist + elist + flist + glist + hlist\
    + ilist + jlist
comp_list.sort()
comp_set = set()
count = 0
for lot_num in comp_list:
    if lot_num in comp_set:
        pass
    else:
        comp_set.add(lot_num)
        if count == 5:
            # print("#################")
            count = 0
        print(f"{lot_num} appears {comp_list.count(lot_num)} times")
        count += 1

comp2_set = set(comp_list)
comp3_set = set()
# print(comp2_set)

print("#####################")
print("Numbers Not Yet Called")
for lot_exclude in range(1, 70):
    if lot_exclude in comp2_set:
        pass
    else:
        comp3_set.add(lot_exclude)
        print(f"{lot_exclude}", end=" ")
print()
