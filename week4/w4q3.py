def square_list(numbers):

    squared_numbers = [x ** 2 for x in numbers]
    return squared_numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_list(numbers)
print(squared_numbers)  
