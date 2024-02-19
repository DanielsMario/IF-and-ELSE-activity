number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    bigger = number1
    if number2 >= number3:
        quite = number2
        smaller = number3
    else:
        quite = number3
        smaller = number2
elif number2 >= number1 and number2 >= number3:
    bigger = number2
    if number1 >= number3:
        quite = number1
        smaller = number3
    else:
        quite = number3
        smaller = number1
else:
    bigger = number3
    if number1 >= number2:
        quite = number1
        smaller = number2
    else:
        quite = number2
        smaller = number1

print(f"The numbers in ascending order are: {smaller}, {quite}, {bigger}")
