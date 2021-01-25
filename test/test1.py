list1 = [2, 4, 4, 9, 4, 8, 8, 8, 7, 4, 6]
list2 = [2, 8, 8, 4, 4, 11, 13]
# list3 = [x for x in list1 if x not in list2]
list3 = set(list1) - set(list2)
# list3 = list1 - list2

# for i in list2:
#     for j in list1:
#         if i == j:
#             list1.remove(j)


# for i in list2:
#     list1.remove(i)

# list1 += list2

print(list3)