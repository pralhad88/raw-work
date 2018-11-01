# start = 0
# new = 1
# count = 0
# while count<11:
# 	print start
# 	sum1 = start + new
# 	start = new
# 	new = sum1
# 	count += 1


##febonaiseries
a=0
b=1
for count in range(11):
	print a
	c=a+b
	a=b
	b=c

### prime number 
x=int(raw_input("enter number"))
s=0
for i in range(2,x):
	if x%i==0:
		s+=1
if s==0:
	print 'prime'
else:
	print "not prime"



for j in range(3,20):
	s = 0
	for i in xrange(2,j-1):
		if j % i ==0:
			s +=1
	if s == 0:
		# print "prime"
		# print j
		if  600851475143 % j == 0:
			print j
			print "l"
	# else:
	# 	print "not prime" 
