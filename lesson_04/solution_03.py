""" Написать функцию xor_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования,
которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. Написать
также функцию xor_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку. """


def xor_cipher(string, key):
    result = ""
    # pass character by character
    for i in string:
        """ 
        1. ord(character) to return the integer representing the Unicode character
        2. ^ (XOR) character by key
        3. chr to convert Unicode integer to Unicode character
        4. add character to result
        """
        result += chr(ord(i) ^ key)
    return result


def xor_uncipher(string, key):
    result = ""
    for i in string:
        result += chr(ord(i) ^ key)
    return result


# Encryption
user_string = input("Enter string to encrypt: ")
user_key = int(input("Enter the encryption key: "))
res = xor_cipher(user_string, user_key)
print("Encrypted string:", res, "\n")

# Decryption
user_string = input("Enter the encrypted string: ")
user_key = int(input("Enter the encryption key: "))
res = xor_uncipher(user_string, user_key)
print("Decrypted string:", res)
