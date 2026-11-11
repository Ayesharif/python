# mini calculator
 
print(" Please enter only given operators (+, -, *, /, ** )")
a= int(input("Enter first value: "))
b= int(input("Enter second value: "))
operator= input("Enter oprator: ").strip()

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "**":
    print(a ** b)
else:
    print("Please Enter the given operators only!")    