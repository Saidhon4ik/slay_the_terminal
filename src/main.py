





print("\n=========================================")
print("Welcome to the Slay The Terminal")
print("It is a fanmade game, so have fun")
print("=========================================\n")

name = input("Enter your name: ")
name = name.strip()
while not name:
    print("Name cannot be empty bro...")
    name = input("Enter your name: ")
    name = name.strip()