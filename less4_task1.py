import random

ran = random.randint(1, 10)
result = int(input('Enter number between (0, 10): '))
while True:
    if result < 0 or result > 10:
        print('ERROR! Wrong value')
        result = int(input('Try again: '))
    if result != ran:
        result = int(input('Try again: '))
    else:
        print(f'Congratulation!!!you guessed it. It was {result}')
        break
