# for i in range(1,20):
#     if(i%2 != 0):
#         print(i)

# for i in range(1,11):
#         print( "57 * ", i , " = ", i*57  )

# for i in range(1,50):
#     if(i == 15):
#         continue
    
#     if(i%3 == 0):
#         print(i)

a= int(input("Enter first value : "))
b= int(input("Enter second value : "))
for i in range(1,1000):
    if(i%a == 0 and i%b == 0):
        print(i)