while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        print("Exit")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if ch == 1:
        print("Result =", a + b)

    elif ch == 2:
        print("Result =", a - b)

    elif ch == 3:
        print("Result =", a * b)

    elif ch == 4:
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", a / b)

    else:
        print("Wrong Choice")