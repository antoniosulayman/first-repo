list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]



similar = list(set(list1) & set(list2))


different = list(set(list1) ^ set(list2))


all_numbers = list(set(list1) | set(list2))

print( similar)
print(different)
print( all_numbers)
