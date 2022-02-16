import random
string = input('Enter some string: ')
new_string = ' '
while len(new_string) <= len(string) * 5:
    if string.isalpha() != True:
        print('ERROR')
        string = input('Enter some string: ')

    new_item = random.choice(string)
    new_string += new_item

first = new_string[0:len(string) + 1]
second = new_string[(len(string) + 1):(len(string)*2 + 1)]
third = new_string[(len(string)*2 + 1):(len(string)*3 + 1)]
fourth = new_string[(len(string)*3 + 1):(len(string)*4 + 1)]
fifth = new_string[(len(string)*4 + 1):(len(string)*5 + 1)]
print(first, second, third, fourth, fifth, end = ' ')
