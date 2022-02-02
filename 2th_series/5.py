import string
import random

def list_gerenrator(counts):
    diff = same = 0

    char_list_1 = random.choices(string.ascii_uppercase, k = counts)
    char_list_2 = random.choices(string.ascii_uppercase, k = counts)

    for i,j in zip(char_list_1,char_list_2):
        if i==j:
            same+=1
        else:
            diff+=1
            
    print(char_list_1,"\n",char_list_2)
    print(f"diffrent is {diff} and the same is {same}")

counts = int(input("lenth:"))
list_gerenrator(counts)