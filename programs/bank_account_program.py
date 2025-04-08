def show_balance(balance):
    print(f"Your balance is  ${balance:.2f}")
    pass


def deposit(balance):
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("That's not a valid amount")
        return 0 #importante retornar zero para o programa n quebrar
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter an amount to be withdraw: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True


    while is_running:
        print("*" *25)
        print("Banking Program")
        print("*" *25)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "4":
            is_running = False

        elif choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit(balance)
        
        elif choice == "3":
            balance -= withdraw(balance)

        else:
            print("Value Error")

    print("Thank you! Have a nice a day !")


if __name__ == '__main__':
    main()