def most_repetitions(my_list: list):
    new_dict = {}

    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1

    max_number = max(new_dict.values())

    for k, v in new_dict.items():
        if v == max_number:
            print(f"{k} has the most repetitions.")

  
        
the_list = [1, 2, 3, 3, 4, 5, 2, 5, 6, 5,"a","b","a","a","a"]
most_repetitions(the_list)

        