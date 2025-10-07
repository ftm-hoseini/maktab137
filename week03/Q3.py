#Bubble_sort
num_list = [6, 5, 4, 3, 2, 1]
def bubble_sort(numbers: list) -> list:
    for i in range(len(numbers)-1):
        counter = 0
        while counter < (len(numbers) - 1):
            if numbers[counter] > numbers[counter + 1]:
                numbers[counter], numbers[counter + 1] = numbers[counter + 1], numbers[counter]
                counter = counter + 1
            else:
                counter = counter + 1

    return numbers
print(bubble_sort(num_list))


#Merge_sort
numberss = [8, 9, 5, 3, 7, 2, 1, 10]
def merge_sort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


print(merge_sort(numberss))

