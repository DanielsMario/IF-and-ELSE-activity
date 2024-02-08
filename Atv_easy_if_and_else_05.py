nota1 = float(input("Enter the student's first grade: "))
nota2 = float(input("Enter the student's second grade: "))

nota = (nota1 + nota2)/2

if nota >= 7 and nota < 10:
    print(f"Your score was {nota}, you are approved! ")
elif nota == 10:
    print(f"Your grade was {nota}, you passed with Distinction!")
elif nota < 7:
    print(f"Your grade was {nota}, your failed!")