import random

def num_guess_game():
    guess_count = 0

    print("Welcome in number guessing game!")

    while True:
        range_input = (input("Choose the range you want to guess in (integer): "))
        try:
            range_input = int(range_input)
            break
        except ValueError:
            print("Invalid input. Try again")
            continue


    number_to_guess = random.randint(1,range_input)
    print(number_to_guess)

    while True:
        user_try = int(input(f"Guess the number from {0} to {range_input}: "))
        if user_try < number_to_guess:
            print("Your number is too small! Continue guessing.")
            guess_count+=1
            continue
        elif user_try > number_to_guess:
            print("Your number is too big! Continue guessing.")
            guess_count+=1
            continue
        else:
            break
    
    print(f"Congrats! You guesses the number correctly. You got {guess_count} tries.")


if __name__ == "__main__":
    num_guess_game()