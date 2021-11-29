sum=0
avg=0
for i in range (1,11):
    n=int(input ('Enter a Number:'))
    sum += n
avg=sum/10
print ("Sum of the Numbers are:{0:5d}".format(sum))
print ("Average of the Numbers are:{0:5.2f}".format(avg))
