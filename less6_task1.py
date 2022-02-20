str1 = input()
new_list = str1.split()
new_set = set(new_list)
dict1 = {i : 1 for i in new_set }
print(dict1)

# from collections import Counter
#
# str2 = input()
# lis2 = str2.split()
# new = dict(Counter(lis2))
# print(new)