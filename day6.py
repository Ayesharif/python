from math import sqrt

# def check_num(num):

#     if(num % 2 == 0):
#         print("It's an Even Number")
#     if(num % 2 != 0):
#         print("It's an Odd Number")



# check_num(22)


# def check_vowels(text):
#     vowels=['a', 'e', 'i', 'o', 'u']
#     count=0

#     for i in set(text):
#         if(i in vowels):
#             count+=1

#     return count    


# print(check_vowels("waoo"))


def average_Mark(marks):
    total=0
    count= 0
    for i in marks:
        total+=i
        count+=1


    print( total/count )     


average_Mark([85,85,74,96,49])