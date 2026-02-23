account_balance = 5000.0
account_holder = "Demo User"
pin_correct = "1234"

# list to track all transactions done in this session
transaction_history = []

def show_menu():
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

# first ask for PIN before anything
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != pin_correct:
    print("Wrong PIN! Access denied.")
else:
    print(f"\nWelcome, {account_holder}!")

    # keep looping till user chooses exit
    while True:
        show_menu()
        option = input("\nChoose option: ")

        if option == "1":
            print(f"\nCurrent Balance: Rs {account_balance:.2f}")

        elif option == "2":
            try:
                deposit_amount = float(input("Enter amount to deposit: Rs "))
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    account_balance += deposit_amount
                    transaction_history.append(f"Deposited: Rs {deposit_amount:.2f}")
                    print(f"Rs {deposit_amount:.2f} deposited successfully.")
                    print(f"New Balance: Rs {account_balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")

        elif option == "3":
            try:
                withdraw_amount = float(input("Enter amount to withdraw: Rs "))
                if withdraw_amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif withdraw_amount > account_balance:
                    # can't withdraw more than what's in account
                    print("Insufficient balance!")
                    print(f"Available: Rs {account_balance:.2f}")
                else:
                    account_balance -= withdraw_amount
                    transaction_history.append(f"Withdrew : Rs {withdraw_amount:.2f}")
                    print(f"Rs {withdraw_amount:.2f} dispensed. Please collect cash.")
                    print(f"Remaining Balance: Rs {account_balance:.2f}")
            except ValueError:
                print("Invalid amount entered.")

        elif option == "4":
            if len(transaction_history) == 0:
                print("No transactions done in this session.")
            else:
                print("\n--- Transaction History ---")
                for idx, txn in enumerate(transaction_history, 1):
                    print(f"  {idx}. {txn}")

        elif option == "5":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option, try again.")