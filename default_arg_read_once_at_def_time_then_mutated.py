def func(val, temp_list=[]):
    temp_list.append(val)
    return temp_list

func(1)

# not accessible, but default temp_list list was mutated and will b
print(temp_list) 

