
from random import seed,randint
# init the empty list
numbers_list=[]
seed(2)
# fill the empty list to rand number
for i in range(100):
    numbers_list.append(randint(0,1000))
print(f"max number in list is: {max(numbers_list)} and the min number is: {min(numbers_list)}")