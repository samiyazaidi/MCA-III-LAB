def sum_of_digits(number):
    number = abs(number)
    
    digit_sum = 0
    
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    
    return digit_sum

num = int(input("Enter an integer: "))

total_sum = sum_of_digits(num)

print(f"The sum of the digits of {num} is: {total_sum}")
