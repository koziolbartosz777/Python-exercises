class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to ATM!")
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)
        print("\nYour account balance is now: ", self.balance)
        

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if amount <= self.balance:
            self.balance-=amount
            print(f"\n{amount} has been withdrawn")
            print(f"\nCurrent balance is: {self.balance}")
        else:
            print("Insufficient balance")
    
    def display_balance(self):
        print(f"\nCurrent account balance: {self.balance}")

if __name__ == "__main__":
    atm = BankAccount()

    while True:
        print("""
        (1) Display balance
        (2) Deposit money
        (3) Withdraw money
        (q) To quit
    """)
        
        user_choice = input("Enter your choice: ").lower()

        if user_choice == "1":
            atm.display_balance()
        elif user_choice == "2":
            atm.deposit()
        elif user_choice == "3":
            atm.withdraw()
        elif user_choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        



