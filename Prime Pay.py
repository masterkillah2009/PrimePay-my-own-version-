class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! Your new balance is: K{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds.")
        else:
            self.balance -= amount
            print(f"Your withdrawal was successful! Your new balance is: K{self.balance}")

    def check_balance(self):
        print(f"Your current balance is: K{self.balance}")


class PrimePay:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter your account number: ")
        initial_balance = int(input("Enter your initial balance: "))
        self.accounts[account_number] = BankAccount(account_number, initial_balance)
        print("Account created successfully!")

    def login(self):
        account_number = input("Enter your account number: ")
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found. Please create an account first.")
            return None

    def run(self):
        while True:
            print("Welcome to PrimePay")
            print("Choose an option:")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")

            option = input("> ")

            if option == "1":
                self.create_account()
            elif option == "2":
                account = self.login()
                if account:
                    while True:
                        print("Choose an option:")
                        print("1. Make A Deposit")
                        print("2. Make A Withdrawl")
                        print("3. Check Your Balance")
                        print("4. Logout")

                        option = input("> ")

                        if option == "1":
                            amount = int(input("Enter the amount to deposit: "))
                            account.deposit(amount)
                        elif option == "2":
                            amount = int(input("Enter the amount to withdraw: "))
                            account.withdraw(amount)
                        elif option == "3":
                            account.check_balance()
                        elif option == "4":
                            break
                        else:
                            print("Invalid option. Please choose a valid option.")
            elif option == "3":
                print("Thank you for using PrimePay!")
                break
            else:
                print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    banking_system = PrimePay()
    banking_system.run()