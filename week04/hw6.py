def check_string(string1: str, string2: str):

    counter = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            counter +=1 

    return counter

print(check_string("aBcD" , "ABcd"))
