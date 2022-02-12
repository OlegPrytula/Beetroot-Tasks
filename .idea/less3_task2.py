tel_number = input('Enter your phone number: ')
if tel_number.isdigit() == True and len(tel_number) == 10:
    print('Well done!')
else:
    print('Error')