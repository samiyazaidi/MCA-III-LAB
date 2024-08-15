def extract_digits_in_reverse(number):
    number = abs(number)
    
    while number > 0:
        digit = number % 10
        print(digit)
        number //= 10

num = int(input("Enter an integer: "))

extract_digits_in_reverse(num)
