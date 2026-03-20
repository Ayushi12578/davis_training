# Function to calculate bonus
def bonus(salary, years):
    if years >= 10:
        b = salary * 0.20
    elif years >= 5:
        b = salary * 0.10
    else:
        b = salary * 0.05
    
    total = salary + b
    print("Bonus =", b)
    print("Total Salary =", total)


# Loop for multiple employees
n = int(input("Enter number of employees: "))

for i in range(1, n + 1):
    print("Employee", i)
    sal = float(input("Enter salary: "))
    exp = int(input("Enter years of experience: "))
    bonus(sal, exp)