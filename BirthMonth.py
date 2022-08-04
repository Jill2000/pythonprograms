group1 = set()
group2 = set()
self = set()

for i in range(3):
	group1.add(input("Enter birth month " + str(i+1) + ": "))
print('')
for i in range(3):
	group2.add(input("Enter birth month " + str(i+1) + ": "))

print(group1)
print(group2)

self.add(input("Enter your birth month: "))

print("Union: " + str(group1 | group2))
print("Intersection: " + str(group1 & group2))
print("Difference: " + str(group1 - group2))

boolean1 = self.issubset(group1)
boolean2 = self.issubset(group2)

if boolean1 == True:
	print("You have the same birth month with one of your classmates")
elif boolean2 == True:
	print("You have the same birth month with one of your classmates")