def sum_nested_list(my_list):
    new_list = []
    
    for item in my_list:
        
        if type(item) == list:
            new_list.extend(sum_nested_list(item))
        else:
            new_list.append(item)

    return new_list
        
    
nested_list =[1, [2, 3], [4, [5]]]
new_list = sum_nested_list(nested_list)
sum_list = sum(new_list)
print(sum_list)