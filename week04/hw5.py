def file_io(func):
    def wrapper(input):

        func_input = input
        func_output = func(input)

        with open("input.txt", "a") as f:
            f.write(func_input + "\n")
        with open("output.txt", "a") as f:
            f.write(func_output + "\n")

        return func_output
    
    return wrapper


@file_io
def process_data(data):
    return data.upper()

user_input = "hi i am fe. just fe!"

print(process_data(user_input))


