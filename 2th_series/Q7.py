def def_1():
    num_list = [1,2,3,4,5]
    new_list = []
    for i in num_list:
        sum_nums = 0
        for j in range(0,i):
            sum_nums+=j
        new_list.append(sum_nums+100)

    return(new_list)

print(def_1())