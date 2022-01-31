new_list = []
for i in range(0,6):
    sum_nums = 0
    for j in range(0,i+1):
        sum_nums+=j
    new_list.append(sum_nums+100)

print(new_list)