from stack import Stack

st2 = Stack()
def revstring(mystr):
    liststr = []
    # Bread the string into characters
    # [liststr.append(mystr[i]) for i in range(0, len(mystr))]
    [st2.push(i) for i in liststr]
    # for ch in mystr:
    #     st2.push(ch)
    return liststr

revstring("hello")
output = ''
while not st2.isEmpty():
    output = output + st2.pop()
print(output)
