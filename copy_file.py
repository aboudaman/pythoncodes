from os.path import exists
prompt = "> "

print("Enter The filename to copy")
filename = input(prompt)
print("Enter Destination filename")
filedestination = input(prompt)

first_file = open(filename)
indata = first_file.read()
print(f"Copying from {filename} to {filedestination}")

print(f"Length of input file is: {len(indata)} bytes long")

print(f"Does the destination file exists {exists(filedestination)}")

second_file = open(filedestination, "w")
second_file.write(indata)
print("done")

# Close files
first_file.close()
second_file.close()
