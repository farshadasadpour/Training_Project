import string
import random

def list_gerenrator():
    D = S = 0

    counts = int(input("lenth:"))
    char_list_1 = random.choices(string.ascii_uppercase, k = counts)
    char_list_2 = random.choices(string.ascii_uppercase, k = counts)

    for i,j in zip(char_list_1,char_list_2):
        if i==j:
            S+=1
        else:
            D+=1
            
    print(char_list_1,"\n",char_list_2)
    print(f"diffrent is {D} and the same is {S}")


list_gerenrator()