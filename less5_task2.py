import random
i = 0
j = 0
list1 = []
list2 = []
while len(list1) <= 10 and len(list2) <= 10:
    i = random.randint(1,100)
    j = random.randint(1,100)
    list1.append(i)
    list2.append(j)
list3 = set(list1) | set(list2)
print(list1,'\n', list2)
print(list(list3))