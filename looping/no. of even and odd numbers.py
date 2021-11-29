cteven=0
ctodd=0
for i in range (1,11):
    n=int(input ('Enter a Number:'))
    if n%2==0:
        cteven +=1
    else:
        ctodd +=1
print ("Even Numbers:{0:5d}".format(cteven))
print ("Odd Numbers:{0:5d}".format(ctodd))
