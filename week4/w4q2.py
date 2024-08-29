def is_first_and_last_same(numbers):
    if len(numbers) == 0:
        return False
    
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 1]
print(is_first_and_last_same(numbers))

numbers = [1, 2, 3, 4, 5]
print(is_first_and_last_same(numbers)) 





