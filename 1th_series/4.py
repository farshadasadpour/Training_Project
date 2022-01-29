import string
import random
S = 0
counts = int(input("Enter:"))
ran = random.choices(string.ascii_letters, k = counts)

for i in range(len(ran)):
    S += ord(ran[i])
print(f"generated str is {ran} and the sum of all ascii is {S}")