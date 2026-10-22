def check_balance(balance):
    print(f"\nYour current balance is: Rs. {balance:.2f}")


def withdraw_money(balance, transactions):
    try:
        amount = float(input("Enter withdrawal amount: Rs. "))
        if amount <= 0:
            print("Error: Amount must be greater than zero.")
        elif amount % 100 != 0:
            print("Error: Enter an amount in multiples of Rs. 100.")
        elif amount > balance:
            print("Error: Insufficient balance.")
        else:
            balance -= amount
            transactions.append(amount)
            print("Please collect your cash.")
            print(f"Remaining balance: Rs. {balance:.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")
    return balance


def show_transactions(transactions):
    print("\n--- Transaction History ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for number, amount in enumerate(transactions, start=1):
            print(f"{number}. Withdrawn: Rs. {amount:.2f}")


def main():
    balance = 10000.0
    correct_pin = "1234"
    transactions = []

    print("===== WELCOME TO PYTHON ATM =====")
    for _ in range(3):
        pin = input("Enter your 4-digit PIN: " )
        if pin == correct_pin:
            print("\nLogin successful!")
            break
        print("Incorrect PIN.")
    else:
        print("Too many incorrect attempts. Access denied.")
        return

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Transaction History")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                check_balance(balance)
            elif choice == 2:
                balance = withdraw_money(balance, transactions)
            elif choice == 3:
                show_transactions(transactions)
            elif choice == 4:
                print("Thank you for using Python ATM!")
                break
            else:
                print("Invalid choice. Select 1 to 4.")
        except ValueError:
            print("Error: Please enter a valid menu number.")


if __name__ == "__main__":
    main()
