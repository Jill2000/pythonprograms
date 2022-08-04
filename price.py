from datetime import datetime, timedelta

fname = (input("Hi what's ur name? "))
lname = (input("What's ur last name? "))
print(' Hi, ' + fname.capitalize() + ' ' + lname.capitalize())
age = input(' How old r u? ')
birthday = input('When is ur birthday? dd/mm/yy: ')
now = datetime.now()
print('Today is: ' + str(now.month) + '/' + str(now.day) + '/' + str(now.year))
print('And your Birthday is: ' + birthday)
place = input('Where do you live?(country) ')
if place == 'philippines':
        city = input('Where in ' + place + '?')
        print()
        if city == 'mindanao':
                mindanao = input('Where in Mindanao? ')
                if mindanao == 'iligan':
                        print('Iliganon mn diay ka bai! ')
                elif mindanao == 'cebu':
                        print('Aw Cebuano diay ka')
                else:
                        print('Aha mana dapita oy')
                gahapon = timedelta(days=1)
                yesterday = now - gahapon
                print('Ang date bitaw gahapon kay ' + str(yesterday))
        elif city == 'luzon':
                luzon = input('Where in Luzon? ')
                print('Oh nice')
        elif city == 'visayas':
                visayas = input('Where in Visayas? ')
                if visayas == 'cebu':
                        print('Aw Cebuano diay ka')
                else:
                        print('Oh nice')
        else:
                print('Ah okay :) ')
else:
        print('Oh great')


