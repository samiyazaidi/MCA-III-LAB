def is_palindrome(number):
    str_num = str(number)
    if str_num == str_num[::-1]:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")