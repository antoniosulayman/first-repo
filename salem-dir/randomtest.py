
#import random
#print(random.random())  
#print(random.randint(1, 10))
#print(random.randrange(10))
#print(random.randrange(1, 10, 2))
#print (random.uniform(1, 10))

#ist = [1,2,3,4,5]
#random.shuffle(list)
#print (list)


#import random

#um = int(input("Enter the number"))
#l=[]
#for l in range(num):
 #   l [l]=random.randrange(num)

#print (l)

#import random

# = int(input("Enter the size of list"))
#a=int(input("enter first number"))
#b=int(input("enter last number"))
#l = random.choices(range(a,b+1),k=s)

#print(l)


# from copy import copy

#my_list = list(range(1, 11))
#print(" 1,10", my_list)
 
#copied_list = copy(my_list)

#random.shuffle(copied_list)
#print("1,10", copied_list)

#sorted_list = sorted(copied_list)
#print("10,1", sorted_list)


#rand_num = random.randint(1, 10)
#print ( 5, rand_num)

import itertools
import string

print(26 ** 4)

i = 0
for var in itertools.product(string.ascii_lowercase, repeat=4):
    i+=1
    print(i, ''.join(var))