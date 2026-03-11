import sqlite3
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "database.db")

class DatabaseManager:
    # Metoda __init__ wykonuje się automatycznie przy tworzeniu obiektu tej klasy
    def __init__(self, db_name="database.db"):
        # Łączymy się z plikiem bazy (lub tworzymy go, jeśli nie istnieje)
        self.conn = sqlite3.connect(db_name)
        # Kursor to narzędzie, przez które wysyłamy komendy SQL do bazy
        self.cursor = self.conn.cursor()
        
        # Od razu przy połączeniu sprawdzamy, czy trzeba stworzyć tabele
        self.create_tables()

    def create_tables(self):
        # Tabela użytkowników. Zwróć uwagę na kolumnę 'salt' (sól), którą dodaliśmy!
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt BLOB NOT NULL
            )
        ''')

        # Tabela na hasła. Klucz obcy (FOREIGN KEY) łączy to hasło z konkretnym użytkownikiem.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vault (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                site TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                notes TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        # Zapisujemy zmiany w bazie
        self.conn.commit()

    def close(self):
        # Zawsze grzecznie zamykamy połączenie, gdy kończymy pracę z bazą
        self.conn.close()

# Ten blok kodu wykona się tylko wtedy, gdy uruchomisz ten plik bezpośrednio.
# Będzie służył nam do przetestowania, czy klasa działa poprawnie.
if __name__ == "__main__":
    # Tworzymy obiekt naszej klasy
    db = DatabaseManager()
    print("Baza danych i tabele zostały pomyślnie utworzone!")
    db.close()