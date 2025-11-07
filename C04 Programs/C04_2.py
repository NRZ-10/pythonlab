class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.acc_no}")
        print(f"Name           : {self.name}")
        print(f"Account Type   : {self.acc_type}")
        print(f"Balance        : ₹{self.balance}")

acc_no = input("Enter Account Number: ")
name = input("Enter Account Holder Name: ")
acc_type = input("Enter Type of Account (Savings/Current): ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(acc_no, name, acc_type, balance)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Display Account\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        account.display()
    elif choice == 4:
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice! Please try again.")

