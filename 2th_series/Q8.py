def def_2():
    num_list = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    for i in range(1,len(num_list)):
        num_list[i]=num_list[i]*num_list[i-1]
    return num_list