l = [1, 2, 3, 4, 5]   

counts = {}
for num in l:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1


duplicates = []

non_duplicates = []

unique_numbers = []

for num, count in counts.items():
    if count > 1:
        duplicates.append(num)
    if count == 1:
        non_duplicates.append(num)
    unique_numbers.append(num)

print ( duplicates)
print ( unique_numbers)
print ( non_duplicates)
