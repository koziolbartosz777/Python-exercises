import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from database import DatabaseManager

class VaultManager:
    def __init__(self, db_manager, user_id, master_password, salt):
        self.db = db_manager
        self.user_id = user_id
        
        # 1. Generowanie klucza na podstawie hasła i soli
        self.key = self._derive_key(master_password, salt)
        
        # 2. Inicjalizacja narzędzia do szyfrowania (Fernet)
        self.cipher = Fernet(self.key)

    def _derive_key(self, password, salt):
        # Funkcja wewnętrzna (KDF), która tworzy bezpieczny klucz z hasła
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000, # Pół miliona iteracji znacząco utrudnia złamanie klucza
        )
        # Fernet wymaga klucza zakodowanego w formacie base64
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def add_password(self, site, username, password, notes=""):
        # Szyfrujemy hasło (Fernet wymaga bajtów, więc używamy .encode())
        encrypted_password = self.cipher.encrypt(password.encode())
        # Notatki też warto zaszyfrować
        encrypted_notes = self.cipher.encrypt(notes.encode()) if notes else b""

        self.db.cursor.execute(
            "INSERT INTO vault (user_id, site, username, password, notes) VALUES (?, ?, ?, ?, ?)",
            (self.user_id, site, username, encrypted_password, encrypted_notes)
        )
        self.db.conn.commit()
        return True, f"Hasło dla strony {site} zostało bezpiecznie zapisane!"

    def get_passwords(self):
        # Pobieramy tylko hasła należące do zalogowanego użytkownika
        self.db.cursor.execute(
            "SELECT id, site, username, password, notes FROM vault WHERE user_id = ?",
            (self.user_id,)
        )
        records = self.db.cursor.fetchall()
        
        decrypted_passwords = []
        for record in records:
            record_id, site, username, enc_password, enc_notes = record
            
            # Odszyfrowujemy dane i zamieniamy z powrotem na tekst (.decode())
            decrypted_password = self.cipher.decrypt(enc_password).decode()
            decrypted_notes = self.cipher.decrypt(enc_notes).decode() if enc_notes else ""
            
            decrypted_passwords.append({
                "id": record_id,
                "site": site,
                "username": username,
                "password": decrypted_password,
                "notes": decrypted_notes
            })
            
        return decrypted_passwords


# --- BLOK TESTOWY ---
if __name__ == "__main__":
    from auth import Authenticator

    db = DatabaseManager()
    auth = Authenticator(db)

    # Rejestrujemy nowego użytkownika tylko do testów sejfu
    auth.register("test_vault", "moje_haslo123")
    
    # Logujemy się, żeby zdobyć sól i ID
    success, msg, user_data = auth.login("test_vault", "moje_haslo123")
    
    if success:
        print("Logowanie udane. Otwieram sejf...")
        
        # Inicjalizujemy sejf
        vault = VaultManager(db, user_data["user_id"], "moje_haslo123", user_data["salt"])
        
        # Dodajemy przykładowe hasła
        vault.add_password("Facebook", "janek123", "P@ssw0rdFB", "Zmienione w 2024")
        vault.add_password("Mój Bank", "jan_kowalski", "SuperTajneBankowe", "PIN: 1234")
        print("Zapisano hasła w bazie (w formie zaszyfrowanej).")
        
        # Odczytujemy hasła
        print("\n--- Zawartość Sejfu ---")
        my_passwords = vault.get_passwords()
        for p in my_passwords:
            print(f"Strona: {p['site']} | Login: {p['username']} | Hasło: {p['password']} | Notatki: {p['notes']}")
    
    db.close()