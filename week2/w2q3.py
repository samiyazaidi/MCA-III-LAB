def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def display_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

display_primes(start_range, end_range)
