num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer:  "))

product = num1*num2

if product <= 5000:
    sum = num1+num2
    print("The sum of integers is: ", sum )
else:
    print("The product is greater than 5000, so no sum is calculated.")
