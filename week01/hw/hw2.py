number: int = int(input("Enter a number: "))
number_list: list = []
for i in range(1, number):
    if number % i == 0:
        number_list.append(i)

if sum(number_list) == number:
    print("yes")
else:
    print("No")