list1 = [10, 23, 45, 66, 77]
list2 = [34, 51, 62, 73, 84]

odd_numbers = [num for num in list1 if num % 2 != 0]

even_numbers = [num for num in list2 if num % 2 == 0]

new_list = odd_numbers + even_numbers

print("New List:", new_list)
