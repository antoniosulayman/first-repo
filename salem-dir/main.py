def my_reverse (l:list):
   for i in range (len(l)//2):
      l[i],l[-i-1] = l [-i-1],[i]
1 = [1,2,3,4,5,6,7,8,]
my_reverse(1)
print(1)