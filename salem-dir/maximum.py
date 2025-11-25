
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
def maximum():
	largest = l[0]
	for num in l:
    		if num > largest:
        		largest = num
	print(largest)
maximum()
