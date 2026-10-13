'''
program to find greatest of 3 number.
'''

num1=int(input("Enter a Number : "))
num2=int(input("Enter a Number : "))
num3=int(input("Enter a Number : "))
if num1>num2 and num1>num3 :
	print("the greater number is :",num1)
elif num2>num1 and num2>num3 :
	print("the greater number is :",num2)
else :
	print("the greater number is :",num3)

