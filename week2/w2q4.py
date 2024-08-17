def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i
        
    return result

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    
    print(f"The factorial of {num} is: {fact}")
