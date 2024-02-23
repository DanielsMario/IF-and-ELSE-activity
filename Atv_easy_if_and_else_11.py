def calculate_increase_salary(wage):
    if wage <= 280:
        percentage_increase = 20
    elif wage <= 700:
        percentage_increase = 15
    elif wage <= 1500:
        percentage_increase = 10
    else:
        percentage_increase = 5

    increase = (percentage_increase / 100) * wage
    new_wage = wage + increase

    return percentage_increase, wage, new_wage

def display_information(wage, percentage_increase, increase, new_wage):
    print(f"Salary before adjustment: R$ {wage}")
    print(f"Increase percentage applied: {percentage_increase}%")
    print(f"Increase value: {increase}")
    print(f"New salary after increase: {new_wage}")

employee_salary = float(input("Enter the employee's salary: R$"))
percentage, increase, new_wage = calculate_increase_salary(employee_salary)
display_information(employee_salary, percentage, increase,  new_wage)