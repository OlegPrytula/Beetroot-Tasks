value = int(input('Enter a value of 5!(factorial of 5): '))
while True:
    if value == 120:
        print(f'You are right, its really {value}')
        break
    else:
        print('You are wrong')
        value = int(input('Think twice: '))