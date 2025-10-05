#q1
user: str = input("Please enter your sentence: ").lower()

char_list: list = []
for chr in user:
    if chr != " " and chr != "":
        if chr == "a" or chr == "o" or chr == "i" or chr == "u" or chr == "e":
            char_list.append(".")
        else:
            char_list.append(chr)


char_list.reverse()
for char in char_list:
    print(char, end="")


