import secrets
import string

def generate_random_password(length=16):
    # Tworzymy zbiór wszystkich znaków: małe/wielkie litery, cyfry i znaki specjalne
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Losujemy znaki z naszego zbioru tyle razy, ile wynosi 'length'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password