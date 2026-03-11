import os
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import sqlite3
from database import DatabaseManager

class Authenticator:
    def __init__(self, db_manager):
        # Klasa Authenticator potrzebuje dostępu do bazy danych, żeby zapisać/odczytać użytkownika
        self.db = db_manager
        # Inicjalizujemy narzędzie do hashowania
        self.ph = PasswordHasher()

    def register(self, username, password):
        # 1. Walidacja: upewniamy się, że użytkownik wpisał cokolwiek
        if not username or not password:
            return False, "Nazwa użytkownika i hasło nie mogą być puste."

        # 2. Generujemy unikalną "sól" (16 losowych bajtów). 
        # Zapiszemy ją w bazie – będzie nam potrzebna później do szyfrowania sejfu.
        salt = os.urandom(16)

        # 3. Hashujemy hasło za pomocą Argon2
        hashed_password = self.ph.hash(password)

        # 4. Próbujemy zapisać użytkownika w bazie
        try:
            self.db.cursor.execute(
                "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
                (username, hashed_password, salt)
            )
            self.db.conn.commit()
            return True, "Rejestracja zakończona sukcesem!"
        except sqlite3.IntegrityError:
            # W database.py ustawiliśmy kolumnę username jako UNIQUE. 
            # Jeśli ktoś poda login, który już istnieje, baza rzuci ten błąd.
            return False, "Taki użytkownik już istnieje. Wybierz inny login."

    def login(self, username, password):
        # 1. Szukamy użytkownika w bazie po loginie
        self.db.cursor.execute(
            "SELECT id, password_hash, salt FROM users WHERE username = ?", 
            (username,)
        )
        user = self.db.cursor.fetchone()

        # Jeśli fetchone() zwróci None, to znaczy, że nie ma takiego loginu
        if user is None:
            return False, "Nieprawidłowa nazwa użytkownika lub hasło.", None

        # Rozpakowujemy dane pobrane z bazy
        user_id, password_hash, salt = user

        # 2. Weryfikujemy, czy podane hasło pasuje do hasha z bazy
        try:
            self.ph.verify(password_hash, password)
            # Zwracamy True, komunikat i słownik z danymi sesji, które przydadzą się w sejfie
            return True, "Zalogowano pomyślnie!", {"user_id": user_id, "salt": salt}
        except VerifyMismatchError:
            # Hasło jest błędne
            return False, "Nieprawidłowa nazwa użytkownika lub hasło.", None

# --- BLOK TESTOWY ---
# Podobnie jak w database.py, ten fragment wykona się tylko przy bezpośrednim uruchomieniu pliku.
if __name__ == "__main__":
    # Otwieramy połączenie z bazą
    db = DatabaseManager()
    auth = Authenticator(db)

    print("--- Test Rejestracji ---")
    success, msg = auth.register("jan_kowalski", "super_tajne_haslo123")
    print(msg)

    print("\n--- Test Logowania ---")
    success, msg, user_data = auth.login("jan_kowalski", "super_tajne_haslo123")
    print(msg)
    
    if success:
        print(f"Dane wyciągnięte do sesji: {user_data}")
    
    print("\n--- Test Złego Hasła ---")
    success, msg, user_data = auth.login("jan_kowalski", "zle_haslo")
    print(msg)

    db.close()