fact=1
n=int(input ('Enter a Number:'))
for i in range (n,fact,-1):
    fact *= i
print ("Factorial of {0:5d} is:{1:5d}".format(n,fact))
