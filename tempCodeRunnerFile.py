import random
import string 

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars_list = list(chars)
key = chars_list.copy()

#ENCRYPT
plain_text = input("Enter your text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text+=key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter your text to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = chars.index(letter)
    plain_text+=chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
