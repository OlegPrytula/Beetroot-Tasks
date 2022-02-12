row = input('input your string: ')
if len(row) < 2:
    print('Empty string')
else:
    print(row[0:2]+row[-2:])
