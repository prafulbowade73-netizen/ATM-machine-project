balance = 10000

while True:
    print("=====ATM MACHINE=====")
    print("check balance")
    print("deposit money")
    print("withdraw money")
    print("exit")   

    choice = int(input("enter your choice: "))


    if choice == 1:
        print("your current balanceis:",balance)

    elif choice == 2:
        amount  = int(input("enter deposit amount:"))
        balance += amount
        print("amount seposited successfully:")
        print("update balance is:",balance)

    elif choice == 3:
        amount = int(input("enter withdraw amount:"))
        if amount <= balance:
           balance -= amount
           print("please collect your cash.")
           print("remaining balance is:",balance)


        else:
            print("insufficent balance")

    elif choice == 4:
        print("thank you for using ATM.")
        break

    else:
        print("invalid choice please try again.")
