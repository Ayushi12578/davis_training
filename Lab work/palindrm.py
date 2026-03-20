# Function to check palindrome
def check_palindrome(x):
    s = str(x)
    rev = ""

    # Using loop to reverse
    for i in s:
        rev = i + rev

    # Using if-else
    if s == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Taking input from user
value = input("Enter number or string: ")

check_palindrome(value)