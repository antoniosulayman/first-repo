l=[5,9,3,7,1,46,8,6,9,6]
def maximum(l):
	max=l[0]
	for i in l:
		if i>max:
			max=i
	print(max)
maximum(l)

