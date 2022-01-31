from random import seed,randint
import operator
dict_number = dict()

seed(None)
for i in range(100):
    dict_number={**dict_number, str(randint(1,1000)):randint(0,10000000000)}

max_value_key = max(dict_number.items(),key=operator.itemgetter(1))[0]
