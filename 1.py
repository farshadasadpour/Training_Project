
from random import seed,randint

numbers_list=[]
seed(2)
for i in range(100):
    numbers_list.append(randint(0,1000))
print(f"max number in list is: {max(numbers_list)} and the min number is: {min(numbers_list)}")