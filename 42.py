'''
Program to Perform  Calculator Operations using Matchcase 
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
ch = int(input("Enter a choice: 1. Addition  2. Subtraction  3. Multiplication  4. Division: "))

match ch:
    case 1:
        res = num1 + num2
        print("The addition of the numbers is:", res)
    case 2:
        res = num1 - num2
        print("The subtraction of the numbers is:", res)
    case 3:
        res = num1 * num2
        print("The multiplication of the numbers is:", res)
    case 4:
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            res = num1 / num2
            print("The division of the numbers is:", res)
    case _:
        print("Invalid choice.")





