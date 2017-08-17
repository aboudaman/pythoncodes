from sys import argv
from os.path import exists

prompt = "> "
print("Enter filename you want to open")
open_file = input(prompt)

txt = open(open_file, "w")
print("Truncating")
txt.truncate()

print("Adding some lines...")
txt.write("I Am Abou \n")
txt.write("Hello beautiful Python\n")
print("\n")
txt.write("Another big up to python\n")


# Close the file
print("Closing The file")
txt.close()
