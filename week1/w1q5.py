def calculate_cubes(n):
    for i in range(1, n + 1):
        cube = i ** 3
        print(f"The cube of {i} is {cube}")

num = int(input("Enter a number: "))

calculate_cubes(num)
