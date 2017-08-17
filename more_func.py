def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args === multiple arguments

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print("Running print_two function")
print_two("hello", "Boo")

print("Running print_two_again")
print_two_again("argument1", "argument2")
