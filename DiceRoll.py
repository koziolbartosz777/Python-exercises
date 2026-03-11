import random

def roll_dice_game():
    print("🎲 Witaj w grze w rzucanie kośćmi! 🎲")

    while True:
        roll_dice = input("\nRoll the dice? ['y'/'n']: ").strip().lower()

        if roll_dice not in ['y','n']:
            print("Invalid input")
            continue

        elif roll_dice == 'n':
            print("Dzięki za grę! Do zobaczenia!")
            break

        elif roll_dice == 'y':
            try:
                user_input = input("Ile kości chcesz rzucić? (Podaj liczbę całkowitą): ")
                num_dice = int(user_input)

                if num_dice <= 0:
                    print("Musisz rzucić przynajmniej jedną kością! Spróbuj ponownie.")
                    continue

                print(f"Rzucam {num_dice} kośćmi...")

                results = [random.randint(1,6) for _ in range(num_dice)]

                print(f"Twoje wyniki: {results}")
                print(f"Suma oczek: {sum(results)}")

            except ValueError:
                print("Błąd: To nie jest poprawna liczba całkowita! Wpisz cyfrę (np. 1, 2).")     
            except Exception as e:
                print(f"Wystąpił niespodziewany błąd: {e}")


if __name__ == "__main__":
    roll_dice_game()