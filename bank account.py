class BankAccount:

    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self):
        amount = float(input("How much would you like to deposit? "))
        self.balance += amount
        print(f"Balance is now {self.balance}")

    def withdrawal(self):
        amount = float(input("How much would you like to withdraw? "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance is now {self.balance}")
        else:
            print(f"You do now have sufficient funds, your balance is {self.balance}")

    def display(self):
        print("The current balance is", self.balance)


revolut = BankAccount()
revolut.deposit()
revolut.withdrawal()
