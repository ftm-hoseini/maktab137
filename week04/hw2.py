def convert_to_string(func):
    def wrapper(*args):

        new_arguments = list(map(str, args))
        return func(*new_arguments)
    
    return wrapper



def len_string(func):
    def wrapper(*args):

        len_arguments = list(map(len, args))
        print(len_arguments)
        return func(*args) 
      
    return wrapper


@convert_to_string
@len_string
def data(name, age):
    print(name +"\t"+ age)

data("Fatemeh", 24)





