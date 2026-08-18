balance = 10000
correct_pin = 1234
attempts = 3

# PIN verification
while attempts > 0:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN!")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Your card is blocked.")
else:

    # ATM Menu
    while True:
        print("\n===== ATM MACHINE =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
                print("Updated balance:", balance)
            else:
                print("Enter a valid amount.")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid amount.")

            elif amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", balance)

            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Please try again.")
