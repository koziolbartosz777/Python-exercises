import random

# Lista słów
words = ["python", "developer", "programming", "hangman", "keyboard", "computer", "function"]
word_to_guess = random.choice(words)

# Lista wyświetlana graczowi
display = ["_"] * len(word_to_guess)

# Liczba żyć
lives = 7

# Zestawy liter
correct_letters = set()
wrong_letters = set()

print("Welcome to Hangman!")
print("Try to guess the word, letter by letter.")
print("You have", lives, "lives.\n")


while "_" in display and lives>0:
    print("Word: ", " ".join(display))
    print("Wrong guesses: ", " ".join(sorted(wrong_letters)))
    guess = input("Enter your guess: ").strip().lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter a single letter (a-z).\n")
        continue

    if guess in correct_letters or guess in wrong_letters:
        print("You already guessed that letter!\n")
        continue

    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.\n")
        correct_letters.add(guess)
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display[i]=guess

    else: 
        print(f"Sorry! '{guess}' is not in the word.\n")
        wrong_letters.add(guess)
        lives-=1

    
    print(f"Lives left: {lives}\n")


if "_" not in display:
    print("You won")
    print("The word was:", word_to_guess)
else:
    print("Game over! You lost!")
    print("The word was:", word_to_guess)