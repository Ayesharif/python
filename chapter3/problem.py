# name= input("enter your name: ")
# print(f"Good afternoon {name}")

letter= '''
Dear <name>
You are selected!
<date>
'''

text =letter.replace("<name>", "Muhamad   Ayesh").replace("<date>", "20 Nov 2025")

print(text.find(" "))

print(text.replace("   "," "))


format= "Dear User! \n  this python course is nice.\n  Thanks"
print(format)

