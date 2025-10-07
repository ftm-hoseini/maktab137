import itertools
import copy
from itertools import combinations
user_words = input("Enter words: ").split()

list_of_words_2 = list(itertools.combinations(user_words, 2))
new_list = list(map(list, list_of_words_2))
shallow_copy_2 = copy.copy(new_list)
deep_copy_2 = copy.deepcopy(new_list)
new_list[0][0] = 'maktab137'

list_of_words_3 = list(itertools.combinations(user_words, 3))

list_of_words_4 = list(itertools.combinations(user_words, 4))


print("list_of_words_2".center(50, "-"))
print(list_of_words_2)
print("list_of_words_3".center(50, "-"))
print(list_of_words_3)
print("list_of_words_4".center(50, "-"))
print(list_of_words_4)
print("shallow copy 2 vs deep copy 2".center(50, "-"))
print(f"shallow copy 2: {list(shallow_copy_2)} \ndeep copy 2: {list(deep_copy_2)}")

