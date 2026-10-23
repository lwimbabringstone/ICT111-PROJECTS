accounts = {}

print("............ AIRTEL MONEY SETUP ............")

phone_numbers = [
    "0123456781", "0964328806", "0978604958"
]

for phone_number in phone_numbers:
    accounts[phone_number] = {
        "balance": 1000.0,
        "password": "1234",
        "last_transfer": None,
    }

logged_in_number = None

while True:
    print("\n............ AIRTEL MONEY ............")
    print("1. Login")
    print("2. Check balance")
    print("3. Send money")
    print("4. Deposit")
    print("5. Reverse last transfer")
    print("6. Change password")
    print("7. Logout")
    print("0. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        phone_number = input("Enter your registered phone number: ").strip()
        if phone_number not in accounts:
            print("This number is not registered.")
            continue
        entered_password = input("Enter password: ").strip()
        if entered_password == accounts[phone_number]["password"]:
            logged_in_number = phone_number
            print(f"Login successful for {phone_number}.")
        else:
            print("Invalid password.")
    elif choice == "2":
        if logged_in_number is None:
            print("Please log in first.")
        else:
            balance = accounts[logged_in_number]["balance"]
            print(f"Balance for {logged_in_number}: K{balance:.2f}")
    elif choice == "3":
        if logged_in_number is None:
            print("Please log in first.")
            continue
        recipient_number = input("Enter recipient phone number: ").strip()
        if recipient_number not in accounts:
            print("Recipient is not one of the 15 registered numbers.")
            continue
        if recipient_number == logged_in_number:
            print("You cannot send money to your own number.")
            continue
        try:
            amount = float(input("Enter amount to send: K"))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > accounts[logged_in_number]["balance"]:
                print("Insufficient balance.")
            else:
                accounts[logged_in_number]["balance"] -= amount
                accounts[recipient_number]["balance"] += amount
                accounts[logged_in_number]["last_transfer"] = {
                    "recipient": recipient_number,
                    "amount": amount,
                }
                print(f"K{amount:.2f} sent to {recipient_number}.")
        except ValueError:
            print("Invalid amount. Enter a number.")
    elif choice == "4":
        if logged_in_number is None:
            print("Please log in first.")
            continue
        try:
            amount = float(input("Enter deposit amount: K"))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                accounts[logged_in_number]["balance"] += amount
                print(
                    f"K{amount:.2f} deposited. New balance: "
                    f"K{accounts[logged_in_number]['balance']:.2f}"
                )
        except ValueError:
            print("Invalid amount. Enter a number.")
    elif choice == "5":
        if logged_in_number is None:
            print("Please log in first.")
            continue
        transfer = accounts[logged_in_number]["last_transfer"]
        if transfer is None:
            print("There is no outgoing transfer to reverse.")
            continue
        recipient_number = transfer["recipient"]
        amount = transfer["amount"]
        if accounts[recipient_number]["balance"] < amount:
            print("Cannot reverse: recipient no longer has enough balance.")
        else:
            accounts[recipient_number]["balance"] -= amount
            accounts[logged_in_number]["balance"] += amount
            accounts[logged_in_number]["last_transfer"] = None
            print(f"Reversed K{amount:.2f} from {recipient_number}.")
    elif choice == "6":
        if logged_in_number is None:
            print("Please log in first.")
            continue
        current_password = input("Enter current password: ").strip()
        if current_password != accounts[logged_in_number]["password"]:
            print("Incorrect current password.")
            continue
        new_password = input("Enter new password: ").strip()
        if new_password:
            accounts[logged_in_number]["password"] = new_password
            print("Password changed successfully.")
        else:
            print("Password cannot be empty.")
    elif choice == "7":
        if logged_in_number is None:
            print("No account is currently logged in.")
        else:
            print(f"Logged out from {logged_in_number}.")
            logged_in_number = None
    elif choice == "0":
        print("Thank you for using Airtel Money.")
        break
    else:
        print("Invalid option. Choose a number from the menu.")

