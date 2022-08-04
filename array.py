import datetime
def printq(name):
	initial = name[0:1].upper()
	return initial
x = datetime.datetime.now()
print(x)
fname = input('enter fname: ')
lname = input('enter lname: ')
aname = input('enter another one: ')
oname = input('enter another one: ')
print('your initial is: ' +printq(fname) + printq(lname) + printq(aname) + printq(oname))	
