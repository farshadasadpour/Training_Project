from operator import le
from random import seed,randint

result=dict()
list_num = []
def list_gerenrator(l=10):
    # init the empty list
    numbers_list=[]
    seed(None)
    # list
    numbers_list = [randint(0,1000) for i in range(l)]
    return numbers_list

total_list = [list_gerenrator() for i in range(2)]

for i in range(len(total_list)):
    result[i+1]=max(total_list[i])
for key,value in result.items():
    list_num.append(value)
    print(f"{key}th number from {key}th list is {value}")
print(f"maximum number is {max(list_num)}")