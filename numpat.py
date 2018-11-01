num=int(input("enter number"))
for i in range(1,num):
		for j in range(i):
			print (i, end=' ')
		print()


# j=4
# i=1
# while i<6:
# 	print ' '*j+('*'*i)
# 	j-=1
# 	i+=1

j=4
for i in range(1,6):
	print(' '*j+('*'*i))
	j-=1