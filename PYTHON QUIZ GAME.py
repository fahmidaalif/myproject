
#  ATM MACHINE

pin = "1234"
balance = 5000

print("=" * 35)
print("     WELCOME TO ABC ATM")
print("=" * 35)

user_pin = input("Enter Your PIN: ")

if user_pin == pin:

    while True:

        print("\n------ MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter Your Choice (1-4): ")

        if choice == "1":
            print(f"\nYour Current Balance: Tk {balance}")

        elif choice == "2":

            amount = float(input("Enter Deposit Amount: "))

            balance += amount

            print(f"Deposit Successful!")
            print(f"New Balance: Tk {balance}")

        elif choice == "3":

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:

                balance -= amount

                print("Withdraw Successful!")
                print(f"Remaining Balance: Tk {balance}")

            else:

                print("Insufficient Balance!")

        elif choice == "4":

            print("\nThank You For Using ABC ATM.")
            break

        else:

            print("Invalid Choice!")

else:

    print("Wrong PIN!")