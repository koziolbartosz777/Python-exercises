import getpass
from database import DatabaseManager
from auth import Authenticator
from vault import VaultManager
from utils import generate_random_password

def vault_menu(db, user_data, master_password):
    # Inicjalizujemy sejf dla zalogowanego użytkownika
    vault = VaultManager(db, user_data["user_id"], master_password, user_data["salt"])
    
    while True:
        print("\n" + "="*20)
        print("🔒 TWÓJ SEJF")
        print("="*20)
        print("1. Dodaj nowe hasło")
        print("2. Pokaż moje hasła")
        print("3. Wygeneruj bezpieczne hasło (pomocnicze)")
        print("4. Wyloguj i zamknij sejf")
        
        choice = input("\nWybierz opcję (1-4): ")
        
        if choice == '1':
            site = input("Nazwa strony/serwisu (np. Netflix): ")
            username = input("Login do serwisu: ")
            password = getpass.getpass("Hasło (ukryte): ")
            notes = input("Notatki (opcjonalnie, wciśnij Enter by pominąć): ")
            
            success, msg = vault.add_password(site, username, password, notes)
            print(f"\n✅ {msg}")
            
        elif choice == '2':
            passwords = vault.get_passwords()
            if not passwords:
                print("\n📭 Twój sejf jest na razie pusty.")
            else:
                print("\n--- 📋 Zapisane Hasła ---")
                for p in passwords:
                    print(f"[{p['id']}] Strona: {p['site']} | Login: {p['username']} | Hasło: {p['password']} | Notatki: {p['notes']}")
                    
        elif choice == '3':
            length_str = input("Podaj długość hasła (wciśnij Enter dla domyślnych 16 znaków): ")
            length = int(length_str) if length_str.isdigit() else 16
            new_pass = generate_random_password(length)
            print(f"\n✨ Wygenerowane hasło: {new_pass}")
            print("(Zaznacz je, skopiuj myszką i użyj przy dodawaniu wpisu!)")
            
        elif choice == '4':
            print("\nZamykanie sejfu... Wylogowano.")
            # Usuwamy obiekt sejfu z pamięci (żeby klucz zniknął z RAM-u)
            del vault
            break
            
        else:
            print("\n❌ Nieznana opcja. Wybierz 1, 2, 3 lub 4.")

def main():
    # Odpalamy bazę i autoryzację na samym początku programu
    db = DatabaseManager()
    auth = Authenticator(db)
    
    while True:
        print("\n" + "="*30)
        print("🛡️  PASSWORD MANAGER CLI  🛡️")
        print("="*30)
        print("1. Zarejestruj się")
        print("2. Zaloguj się")
        print("q. Wyjdź z programu")
        
        choice = input("\nWybierz opcję (1, 2 lub q): ")
        
        if choice == '1':
            print("\n--- REJESTRACJA ---")
            username = input("Wymyśl login: ")
            # getpass sprawia, że znaki nie pojawiają się w terminalu!
            password = getpass.getpass("Wymyśl hasło główne (ukryte): ") 
            
            success, msg = auth.register(username, password)
            if success:
                print(f"✅ {msg}")
            else:
                print(f"❌ {msg}")
            
        elif choice == '2':
            print("\n--- LOGOWANIE ---")
            username = input("Twój login: ")
            password = getpass.getpass("Twoje hasło główne (ukryte): ")
            
            success, msg, user_data = auth.login(username, password)
            
            if success:
                print(f"✅ {msg}")
                # Po udanym logowaniu przechodzimy do pod-menu sejfu
                vault_menu(db, user_data, password)
            else:
                print(f"❌ {msg}")
                
        elif choice.lower() == 'q':
            print("\nDo widzenia! 👋")
            break
            
        else:
            print("\n❌ Nieznana opcja.")
            
    # Gdy pętla główna się skończy (użytkownik wpisze 'q'), zamykamy bazę
    db.close()

if __name__ == "__main__":
    main()