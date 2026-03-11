# import random
# import string 

# chars = " " + string.ascii_letters + string.punctuation + string.digits
# chars_list = list(chars)
# key = chars_list.copy()

# random.shuffle(key)

# #ENCRYPT
# plain_text = input("Enter your text to encrypt: ")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text+=key[index]

# print(f"Original message: {plain_text}")
# print(f"Encrypted message: {cipher_text}")

# #DECRYPT
# cipher_text = input("Enter your text to encrypt: ")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text+=chars[index]

# print(f"Encrypted message: {cipher_text}")
# print(f"Original message: {plain_text}")
#----------------------------------------------------------------------------
from cryptography.fernet import Fernet


class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.strip().split(":")
                decrypted = Fernet(self.key).decrypt(encrypted.encode()).decode()
                self.password_dict[site] = decrypted

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict.get(site, "Password not found")


def main():

    passwords = {
        "email": "1234567",
        "facebook": "facebookpass",
        "youtube": "ytpass",
        "someaccount": "somepass"
    }

    pm = PasswordManager()

    print("""
What do you want to do?
(1) Create a new key
(2) Load an existing key
(3) Create new password file
(4) Load existing password file
(5) Add a new password
(6) Get a password
(q) Quit
""")

    done = False

    while not done:

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter key file path: ")
            pm.create_key(path)
            print("Key created")

        elif choice == "2":
            path = input("Enter key file path: ")
            pm.load_key(path)
            print("Key loaded")

        elif choice == "3":
            path = input("Enter password file path: ")
            pm.create_password(path, passwords)
            print("Password file created")

        elif choice == "4":
            path = input("Enter password file path: ")
            pm.load_password_file(path)
            print("Password file loaded")

        elif choice == "5":
            site = input("Enter site: ")
            password = input("Enter password: ")
            pm.add_password(site, password)
            print("Password added")

        elif choice == "6":
            site = input("Enter site: ")
            print("Password:", pm.get_password(site))

        elif choice == "q":
            done = True


if __name__ == "__main__":
    main()