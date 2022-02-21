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


def sum_of_values(dictionary1, dictionary2):
    l1 = []
    l2 = []
    l3 = list(dictionary1)
    for i in dictionary1:
        l1.append(dictionary1[i])
    for j in dictionary2:
        l2.append(dictionary2[j])
    total = [i*j for i, j in zip(l1, l2)]
    for i in range(len(total)):
        print(l3[i], end=' ')
        print(total[i])




print(sum_of_values(stock, prices))
