name="Shivam"
ph_no = "98765432"
order_list=[]
def inputs_():
    #name = input("Enter Customer's name : ")
    #ph_no = input("Enter phone number : ")
    no_order = int(input("How many dishes are orderd : "))
    for x in range (no_order):
        dish_name = input("Enter Number dish name : ")
        dish_price = int(input("Enter price of dish per plate : "))
        no_plate = int(input("How many plates ordered : "))
        total_price = dish_price*no_plate
        order_list.append([x+1 , dish_name , dish_price ,no_plate , total_price])

def total_bill():
    global t
    t=0
    l=len(order_list)
    for r in range(0,l):
        print(order_list[r][4])
        t = t + (order_list[r][4])
def bill_print():
    inputs_()
    print('''
         XYZ RESTURANT 
    
    Customer's Name : '''+name+'''
    Contact number : '''+ph_no)
    for i in order_list:
        print(i)
    total_bill()
    t_str=str(t)
    print("Total Bill amount : "+ t_str )

bill_print()
