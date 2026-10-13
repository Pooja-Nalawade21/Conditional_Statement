'''
program to check grades based on marks.
'''

mark=int(input("Enter the marks of student : "))
if  mark >80 :
	print("The Grade is A.")
elif mark > 65 :
	print("The Grade is B.")
elif  mark > 40 :
        print("The Grade is C.")
else :
	print("Fail.")