num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = int(input("Enter Your Number : "))

if n > len(num):
    print("Error !")
else:
    list1 = num[-n:] + num[:-n]
    print(list1)
