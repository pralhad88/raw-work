# Tack a input form user and, your name and print your initial name and finally sourname. 
# example:- INPUT:- "Pralhad Bharmal Jadhav"
# OUTPUT:- "P. B. Jadhav"

name = input("")
name = name.split()
joint = ''
for i in range(len(name)):
	if i <= (len(name)-2):
		r = name[i][0]+'. '
		joint = joint + r
	elif i == (len(name)-1):
		r = name[len(name)-1]
		joint = joint + r
print(joint)


# YOU CAN PRINT LIST IN VERRTICAL MANNAR WITHOUT USING ANY LOOP IN PYTHON 

LIST =["Geeks", "for", "Geeks"] 
print(*LIST, sep = "\n")