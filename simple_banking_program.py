def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    while True:
        if amount<=0:
            print("You can't deposit amount <= 0. Try again")
            continue
        else:
            print(f"{amount} was deposited into you bank account")
            return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    while True:
        if amount<=0:
            print("You can't withdraw amount <= 0")
            continue
        elif amount > balance:
            print("You can't withdraw amount that is higher than your balance")
            continue
        else:
            print(f"{amount} has been withdrawn from your account")
            return amount



def main():
    balance = 0
    is_running = True


    while is_running:

        print("\n--- Banking Program ---")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your option: ").strip()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+=deposit()
        elif choice == "3":
            balance-=withdraw(balance)
        elif choice == "4":
            is_running = False
            print("Goodbye!")
        else:
            print("Invalid input. Try again.")



if __name__ == "__main__":
    main()