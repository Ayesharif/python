# roll_numbers = [101, 102, 103, 104, 105, 101]

# unique= set(roll_numbers)
# print(list(unique))


employee=[
(101, "Ali", 10000),
(102, "Ali", 20000),
(103, "Ali", 30000),
(104, "Ali", 40000),
(105, "Ali", 50000),
]

employee_id= int(input("Enter Id to Search your record : "))
for i in employee:
    for record in i:
        if(employee_id == record):
            print(i)
            break



# print( employee_id in employee)