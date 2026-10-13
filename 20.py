'''
program to check ticket price based on age
'''

age=int(input("Enter your age : "))
if age < 5:
    print("Ticket is free.")
elif age <=18 :
	print("Ticket price is 120rs.")
else :
	print("Ticket price is 200rs.")
