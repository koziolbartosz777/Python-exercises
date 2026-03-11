import random

quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Who created Python?",
        "options": ["A. Elon Musk", "B. Bill Gates", "C. Guido van Rossum", "D. Mark Zuckerberg"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. CO2", "C. H2O", "D. HO"],
        "answer": "C"
    },
    {
        "question": "Which country invented pizza?",
        "options": ["A. France", "B. Italy", "C. Spain", "D. USA"],
        "answer": "B"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What programming language is named after a comedy group?",
        "options": ["A. Java", "B. C++", "C. Ruby", "D. Python"],
        "answer": "D"
    },
    {
        "question": "Which animal is known as the king of the jungle?",
        "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Gorilla"],
        "answer": "A"
    },
    {
        "question": "What is the fastest land animal?",
        "options": ["A. Lion", "B. Horse", "C. Cheetah", "D. Leopard"],
        "answer": "C"
    },
    {
        "question": "Which planet is the largest in the Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Neptune"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 9", "D. 8"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Power Unit", "D. Control Processing Unit"],
        "answer": "A"
    }
]

def trivia_game():
    score = 0 
    
    random.shuffle(quiz)

    for q in quiz:
        print("\n" + q["question"])
        
        for option in q["options"]:
            print(option)

        guess = input("Enter your answer: ").strip().upper()

        if guess == q["answer"]:
            print("Correct!")
            score+=1
        else: 
            print("Wrong!")
            print("The correct answer was: ", q["answer"])

    print(f"\n Your score: {score/len(quiz)*100:.0f}%")

trivia_game()