def is_palindrome():
    word = input("Enter your word: ").strip().lower()
    
    if word==word[::-1]:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")

is_palindrome()

