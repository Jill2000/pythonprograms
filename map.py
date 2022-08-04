students = {}
index = 0;
print()
print()
for i in range(3):
	snum = input("Enter student number " + str(i+1) + ": ")
	sname = input("Enter first name " + str(i+1) + ": ")
	students[str(snum)] = str(sname)
	get = str(snum)

del students[str(get)]

print("Student List:")

for x,y in students.items():
	print(x, y)
