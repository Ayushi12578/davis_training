# Function to print table
def table(n):
    if n < 0:
        print("Negative number not allowed")
    else:
        for i in range(1, 11):
            print(n, "x", i, "=", n * i)

# Taking input from user
num = int(input("Enter a number: "))

# Calling function
table(num)