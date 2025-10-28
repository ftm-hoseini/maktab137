
def file_io(input_file, output_file):
    def decoraror(func):
        def wrapper(input):

            func_input = input
            func_output = func(input)

            with open("input.txt", "a") as f:
                f.write(func_input + "\n")
            with open("output.txt", "a") as f:
                f.write(func_output + "\n")

            return func_output
        return wrapper
    return decoraror



@file_io(input_file= 'input.txt', output_file='output.txt')
def process_data(data):
    return data.upper()

user_input = "i am fe. just fe!"

process_data(user_input)


