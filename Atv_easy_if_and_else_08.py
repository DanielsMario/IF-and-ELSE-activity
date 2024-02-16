num1 = float(input("Enter the value first of the first product: "))
num2 = float(input("Enter the value of the second product: "))
num3 = float(input("Enter the value of the third product: "))
def number(num1,num2,num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <=num3:
            return num2
    else:
         return num3
smaller_value = number(num1,num2,num3)

print(f"The product with the lowest value is {smaller_value}")