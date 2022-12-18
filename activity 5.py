import random
def generate_random():
    return random.randint(1, 6)
running = True
while running:
    print("DICE SIMULATOR")
    print("1. Roll the dice")
    print("2. Quit")
    choice = input("Please enter your choice: ")
    if choice == "1":
        print("You rolled a", generate_random())
    elif choice == "2":
        running = False
    else:
        print("Invalid input")