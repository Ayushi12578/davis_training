
# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True
# Taking input from user
num = int(input("Enter a number: "))

# Using if-else to display result
if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")