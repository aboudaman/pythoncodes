from sys import argv
script, user_name = argv

prompt = '> '

print(f"Hello {user_name}, I'm the Pink Daaddy {script}")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("What kind of computer you have?")
computer = input(prompt)

print(f"""
    Alright so you like me, {likes} and lives in {lives}
    and you have a {computer} computer.  Nice!!!
""")
