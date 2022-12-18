def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
running = True
while running:
    print("""
        Please select an operation:
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit
        """)
    choice = input("Please enter your choice: ")
    if choice == "1":
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        print(add(a, b))
    elif choice == "2":
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        print(subtract(a, b))
    elif choice == "3":
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        print(multiply(a, b))
    elif choice == "4":
        a = int(input("Please enter your first number: "))
        b = int(input("Please enter your second number: "))
        print(divide(a, b))
    elif choice == "5":
        running = False
    else:
        print("Invalid input")