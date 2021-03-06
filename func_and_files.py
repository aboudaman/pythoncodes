from sys import argv

script, filename = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(filename)

print("All the file")
print_all(current_file)

print("Rewinding.....")
rewind(current_file)

print("Printing Line One")
current_line = 1
print_a_line(current_line, current_file)
print("Printing Line Three")
print_a_line(current_line + 1, current_file)
