import random
i = 0
list1 = []
while len(list1) <= 10:
    i = random.randint(1,100)
    list1.append(i)
print(list1)
print(max(list1))