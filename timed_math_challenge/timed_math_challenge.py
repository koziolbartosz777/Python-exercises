import random
import time
import json

operators = ["+", "-", "*"]
min_operand = 1
max_operand = 15

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)

    calculate_difficulty = calculate_difficulty(left, right, operator)
    
    return expression, answer, calculate_difficulty

def calculate_difficulty(left, right, operator):
    difficulty = 1.0

    if operator in ["+", "-"]:
        if left>9:
            difficulty+=0.5
        if right>9:
            difficulty+=0.5
    elif operator == "*":
        if left in [1,10] or right in [1,10]:  #only 1 or 10 for left of right operand
            difficulty+=0.7
        elif left == 11 or right == 11:
            difficulty+=1.5
        elif left > 11 or right > 11:
            difficulty+=4.0
        else:
            difficulty += 1.9

    return difficulty



while True: 
    problems_count = input("Enter how many problems you want to solve ('q' to quit): ")
    if problems_count.strip().lower( )== 'q':
        quit()
    
    problems_count = int(problems_count)
    print(f"I will generate {problems_count} math problems to solve!")
    start_input = input("Press any key to start!")
    start_time = time.time()

    wrong_guesses = 0
    right_guesses = 0

    for i in range (problems_count):
        expression, answer = generate_problem()
        first_try = True
        
        while True:
            user_guess = input("Problem #" + str(i+1) + ": " + expression + " = ")
            if user_guess == str(answer):
                if first_try:
                    right_guesses+=1
                break
            else:
                wrong_guesses+=1
                first_try = False
                print("Wrong guess, try again!")
                continue

    end_time = time.time()
    total_time = end_time - start_time
    #Counting the percentage based on fist_time correct guesses
    accuracy = (right_guesses/problems_count)*100
    final_score = (accuracy * problems_count * 100)/total_time
    print(f"Your first_time answers percentage: {accuracy} %")
    print(f"Total mistakes made: {wrong_guesses}") #not first-time correct answer counter
    print(f"This test took you {total_time:.2f} seconds")
    print(f"This try score: {round(final_score)}")

    while True:
        print("""
        (s) Save
        (r) Retry
        (q) Quit\n""")

        save_retry_quit_choice = input("Enter your choice: ")

        if save_retry_quit_choice == 'q':  #quit option
            print("Thanks for playing! Bye :)")
            exit()
        elif save_retry_quit_choice == "r": #retry
            break
#Introducing the logic of recording resulst and ranking 
        elif save_retry_quit_choice == 's':
            user_name = input("Enter your name/nickname: ").strip().lower()


            user_results = {
                "Competitor name": user_name,
                "Accuracy" : accuracy,
                "Time": round(total_time, 2),
                "Score": round(final_score)
            }
            #saving resulst into challenge_results file in order to add them to ranking
            try:
                with open('timed_math_challenge/challenge_results.json', 'r') as file:
                    leaderboard = json.load(file)
            except FileNotFoundError:
                leaderboard = []

            leaderboard.append(user_results)

            with open('timed_math_challenge/challenge_results.json', 'w') as file:
                json.dump(leaderboard, file, indent=4)

            print("\nSaved successfully in JSON file.")


            leaderboard.sort(key=lambda x: x["Score"], reverse=True)

            print("\n🏆 --- TOP 3 RANKING --- 🏆")
            
            for index, player in enumerate(leaderboard[:3]):
                print(f"{index+1}. {player['Competitor name']} | Points: {player['Score']} | Time: {player['Time']} seconds")
            print("-"*25 + "\n")

            break



