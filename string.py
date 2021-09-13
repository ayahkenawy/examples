
value = int(input('Enter a number: '))
print(value * 10)
#-----------------------------------------------
first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize award: '
print(first_name.capitalize())
print(last_name.capitalize())
print(note.find('award: '))
print(note.rfind('award: '))
print(note[7:])
#----------------------------------------------------
import re
five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
five_expression =r'\d{5}'
print(re.search(five_expression,five_digit_zip))
print(re.search(five_expression,nine_digit_zip))
print(re.search(five_expression,phone_number))
#---------------------------------------------------
#challenge
miles =float(input('Enter a distance in miles: '))
kilometers_value = miles * 1.609344
print('Value in kilometers : ')
print(kilometers_value)