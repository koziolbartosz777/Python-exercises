# import random

# def rock_paper_scissors_game():
#     available_choices = ['r', 'p', 's']

#     print("✌️ Witaj w grze Kamień, Papier, Nożyce! ✋")

#     while True: 
#         comp_choice = random.choice(available_choices)
#         # print(f"\n Computer choice: {comp_choice}")
#         user_input = input("\n Rock, paper, scissors? (r/p/s) - 'q' to quit: ")

#         if user_input == 'q':
#             print("Thanks for the game. See you later.")
#             break

#         if user_input not in available_choices:
#             print("Invalid input. Try again")
#             continue

#         if user_input == comp_choice:
#             print("\n It's a draw!")
#         elif (user_input == 'r' and comp_choice == 's') or (user_input == 'p' and comp_choice == 'r') or (user_input == 's' and comp_choice == 'p'):
#             print("\n Congrats! You won.")
#         else:
#             print("\n You lost this time!") 

            
# if __name__ == "__main__":
#     rock_paper_scissors_game()


#### better rock,paper,scissors

import random

emojis = {'r': '🪨', 'p': '📝', 's': '✂️'}
choices = ('r', 'p', 's')

def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissors? (r/p/s / 'q' to quit): ").strip().lower()
        if user_choice in choices:
            return user_choice
        elif user_choice == 'q':
            return None
        else:
            print("Invalid choice! Try again.")


def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == 'r' and computer_choice == 's' or user_choice == 'p' and computer_choice == 'r' or user_choice == 's' and computer_choice == 'p'):
        print("You won!")
    else:
        print("You lost!")

def play_game():
    while True:
        user_choice = get_user_choice()
        
        if user_choice is None:
            print("Thanks for playing!")
            break
        computer_choice = random.choice(choices)
        
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)


play_game()

