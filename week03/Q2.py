from copy import deepcopy

sentence = "A decorator is a function, that takes another function as input and returns a new function.!"
list_words = ["function","decorator" ]

'''cache_dict = {}

def cache(func):
    def wrapper(sentence, list_word):
        key = (sentence, list_word)
        if key in cache_dict:
            result = deepcopy(cache_dict[key])
            return result
        else:
            result = func(sentence, list_word)
            
            return result
    return wrapper
'''


def num_of_word(sentence: str, list_word) -> dict:
    new_sentence = ""
    my_dict = {}
    for char in sentence:
        if char.isalpha() or char.isspace():
            new_sentence += char
        else:
            new_sentence += "\t"

    new_sentence = new_sentence.lower()
    new_sentence = new_sentence.split()

    for word in new_sentence:
        if word in list_word:
            my_dict[word] = my_dict.get(word, 0) + 1

    return my_dict

print(num_of_word(sentence, list_words))

