import random
class BankAccount:
    def __init__(self):
        self.account = []

    def create_account(self):
        full_name = input("Please enter your full name: ")
        account_number = random.randint(48001000, 48001100)
        index = len(self.account) + 1
        self.account.append({"full_name": full_name, "account_number": account_number, "balance": 0.0})
        print(f"Your account number is: {account_number}")
        
    def find_account(self):
        full_name = input("Please enter your full name: ")
        find_account = list(filter(lambda account: account["full_name"] == full_name, self.account))
        if find_account:
            for account in find_account:
                print(f"You have an account with this number {account['account_number']} in this bank and balance is {account['balance']}")
        else:
            print(f"Sorry you don't have any account in this bank.")

    def deposit(self):
        account_number = int(input("Please enter your account number you want to deposit into: "))
        add_deposit = float(input("Please enter the amount you want to deposit: "))
        account = next((account for account in self.account if account["account_number"] == account_number), None)
        if account_number:
            account['balance'] += add_deposit
            print(f"Deposit successfully done.")
            print(f"Account balance: {account['balance']}")
        else:
            print(f"Your account number not found!")

    def transfer(self):
        account_number = int(input("Please enter your account number you want to deposit into: "))
        transfer_money = float(input("Please enter the amount you want to transfer: "))
        account = next((account for account in self.account if account['account_number'] == account_number), None)
        if account['balance'] - transfer_money < 0:
            print("Your balance is less than your transfer amount.")
        elif account_number:
            account['balance'] -= transfer_money 
            print(f"Transfer successfully done")
            print(f"Account balance: {account['balance']}")
        else:
            print("Your account number not found!")
        
    def close_account(self):
        account_number = int(input("Please enter your account number you want to close: "))
        account = self.account.pop(next((account for account in self.account if account["account_number"] == account_number), None))
        print(f"Account successfully is closed.")

    def show_all_accounts(self):
        for index, item in enumerate(self.account, 1): 
            print(f"{index}. {item['full_name']}, {item['account_number']}, {item['balance']}")

    def menu(self):
        while True:
            print("1= Create account\n2= Find account\n3= Deposit \n4= Transfer money\n5= Close account\n6= show all accounts\n7= exit")
            try:
                user_input = int(input("Please enter your choice: "))
                if user_input == 1:
                    self.create_account()
                elif user_input == 2:
                    self.find_account()
                elif user_input == 3: 
                    self.deposit()
                elif user_input == 4:
                    self.transfer()
                elif user_input == 5:
                    self.close_account()
                elif user_input == 6:
                    self.show_all_accounts()
                elif user_input == 7:
                        break
                else: print("Enter a valid number.")
            except:
                print("Please enter a valid value.")    

bank_account = BankAccount()
bank_account.menu()

