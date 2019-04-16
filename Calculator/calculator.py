import math

running = True
while running == True:
    start = input(print("""
    Please enter the proper number or operation name:
    1 - addition
    2 - subtraction
    3 - multiplication
    4 - division
    5 -  square
    6 - square root
    q - quit"""))
    if start == "1" or start == "addition":
        number1 = int(input("Please enter first number: "))
        number2 = int(input("Please enter second number: "))
        print("The result is:", number1 + number2)
    elif start == "2" or start == "substraction":
        number1 = int(input("Please enter first number: "))
        number2 = int(input("Please enter second number: "))
        print("The result is:", number1 - number2)
    elif start == "3" or start == "multiplication":
        number1 = int(input("Please enter first number: "))
        number2 = int(input("Please enter second number: "))
        print("The result is:", number1 - number2)
    elif start == "4" or start == "divison":
        number1 = int(input("Please enter first number: "))
        number2 = int(input("Please enter second number: "))
        print("The result is:", number1 / number2)
    elif start == "5" or start == "square":
        number1 = int(input("Please enter number: "))
        print("The result is:", number1 * number1)
    elif start == "6" or start == "square root":
        number1 = int(input("Please enter number: "))
        print("The result is:", math.sqrt(number1))
    elif start == "q" or start == "quit":
        running = False
        break
    else:
        print("Wrong operation")
        start = input("Please input proper number/operation name: ")
