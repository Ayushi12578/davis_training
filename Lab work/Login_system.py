username = "admin"
password = "1234"

attempts = 0

while attempts < 3:
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        print("Wrong Login")
        attempts = attempts + 1

if attempts == 3:
    print("Account Locked")