i = 0
l = []
l2 = []
while i <= 100:
    l.append(i)
    if l[i] % 7 == 0 and l[i] % 5 != 0:
        l2.append(i)
    i +=1
print(l2)