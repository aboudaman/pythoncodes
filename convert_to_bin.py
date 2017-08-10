from stack import Stack

binary = Stack()

def convert_to_bin(num):
    while num > 0:
        bi = num % 2
        binary.push(bi)
        num = num // 2
    return True
convert_to_bin(42)

output = ''
while not binary.isEmpty():
    output = output + str(binary.pop())

print(output)
