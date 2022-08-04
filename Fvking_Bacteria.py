your_variable = int(input('Enter initial count of bacteria: '))

your_variable_hours = int(input('Enter the number of hours: '))

print('The number of bacteria per hour will be: ')

yourn = int((your_variable_hours*60)/ 20)
blindryhme = int(your_variable_hours**yourn)

for i in range(5):
  print(blindryhme)
  blindryhme = blindryhme + (2**yourn)


