import random
import string

def generate_password():
    upper_case_letters = random.choices(string.ascii_uppercase, k=2)  
    digits = random.choices(string.digits, k=1) 
    special_symbols = random.choices(string.punctuation, k=1) 
    lower_case_letters = random.choices(string.ascii_lowercase, k=6) 

    password_list = upper_case_letters + digits + special_symbols + lower_case_letters

    random.shuffle(password_list)

    password = ''.join(password_list)

    return password

password = generate_password()
print(f"Generated Password: {password}")
