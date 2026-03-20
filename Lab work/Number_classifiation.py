#number classification programe
def check_number(num):
    if num>=1:
        print("positive")
    elif num <0:
        print("negative")
    else:
        print("Zero")
    if num!=0:
            if num %2==0:
                print("Even")
            else:
                print("odd")
number = input("Enter numbers separated by space: ").split()
for i in number:
    check_number(int(i))

