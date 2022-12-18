allowed_roll_numbers = list(range(91041, 91091))
student_list = [] 
def binary_search(target, list): 
    low = 0
    high = len(list) - 1
    while low <= high: 
        mid = (low + high) // 2
        if list[mid] == target: 
            return True
        elif list[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return False
running = True
while running: 
    print("""
        EXAM HALL MANAGEMENT SOFTWARE
        --------------------------------
        Allowed Roll number : From 91041 to 91091  
        1. Add a new student
        2. Delete the roll number of student
        3. Display the number of students
        4. Display the largest and smallest roll number present in the hall
        5. Display a sorted list of roll numbers
        6. Quit
        """)
    choice = int(input("Enter your choice: ")) 

    if choice == 1: 
        roll_number = int(input("Enter the roll number: ")) 
        if binary_search(roll_number, allowed_roll_numbers): 
            if binary_search(roll_number, student_list): 
                print("Student already exists") 
            else: 
                student_list.append(roll_number) 
                print("Student added successfully") 
        else:
            print("Roll number not allowed") 
 
    elif choice == 2: 
        roll_number = int(input("Enter the roll number: ")) 
        if binary_search(roll_number, student_list): 
            student_list.remove(roll_number)
    
    elif choice == 3: 
        print("Total number of list : " +len(student_list))
    
    elif choice == 4: 
        print("Largest Roll number :"+max(student_list))
        print("Smallest Roll number :"+min(student_list))
    
    elif choice == 5:
        print(sorted(student_list))