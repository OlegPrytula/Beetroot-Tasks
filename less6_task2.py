stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}



def sum_of_values(dictionary):
    l = []
    for i in dictionary:
        l.append(dictionary[i])
    print(l)
    return sum(l)

print(sum_of_values(prices))
print(sum_of_values(stock))
# another approach

#
# def suma(dict1):
#     values = dict1.values()
#     return sum(values)
#
# print(suma(stock))
# print(suma(prices))