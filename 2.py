
from random import seed,randint

# init the empty list
numbers_list=[]
seed(2)
# fill the empty list to rand number
for i in range(10):
    numbers_list.append(randint(0,1000))
print("befor {}".format(numbers_list))

for i in range(0,len(numbers_list),2):
    swap = numbers_list[i]
    numbers_list[i] = numbers_list[i+1]
    numbers_list[i+1] = swap
print("after {}".format(numbers_list))