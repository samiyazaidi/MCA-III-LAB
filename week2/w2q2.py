def count_digits(num):
    num = abs(num)
    count = 0

    if num == 0:
        return 1
    
    while num > 0:
        num //= 10
        count +=1
    return count

num = int(input("Enter an integer: "))

digit_count = count_digits(num)

print("Total number of digits:", digit_count)
