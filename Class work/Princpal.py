# function to calculate simple interest
def calculateSi(p,r,t):
  return((p*r*t)/100)
#-----------------
#Main program
principle=float(input("Enter principle(in rs):"))
rate=float(input("Enter principle(in %):"))
time=int(input("Enter principle(in year):"))
print("Simple Interest:Rs",calculateSi(principle,rate,time))