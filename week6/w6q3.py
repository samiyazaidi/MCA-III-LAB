def sum_of_squares_of_digits(num):
    num_str = str(num)
    
    first_two_digits = int(num_str[:2])  
    last_two_digits = int(num_str[2:])    
    
    result = (first_two_digits ** 2) + (last_two_digits ** 2)
    
    print(f"Sum of squares of {first_two_digits}^2 and {last_two_digits}^2 is: {result}")

number = int(input("Enter a 4-digit number: "))

sum_of_squares_of_digits(number)
