def encrypt_string(main_string, symbol):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol 
    return encrypted_string

def decrypt_string(encrypted_string, symbol):
    decrypted_string = encrypted_string.replace(symbol, "")  
    return decrypted_string

main_string = input("Enter the main string: ")
symbol = input("Enter a short symbol-based string for encryption: ")

encrypted_string = encrypt_string(main_string, symbol)
print(f"Encrypted String: {encrypted_string}")

decrypted_string = decrypt_string(encrypted_string, symbol)
print(f"Decrypted String: {decrypted_string}")
