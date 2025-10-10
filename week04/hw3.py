def most_repetitions(my_list: list):
    new_dict = {}

    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    res = max(new_dict.values())

    for k, v in new_dict.items():
        if v == res:
            print(f"{k} has the most repetitions.")

  
        
the_list = [1, 2, 3, 3, 4, 5, 2, 5, 6, 5, 2, 2]
most_repetitions(the_list)

        