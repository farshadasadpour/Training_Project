from random import seed,randint

dict_number = dict()

seed(None)
for i in range(100):
    dict_number={**dict_number, str(randint(1,10)):randint(0,10000000000)}
print(dict_number)