class bank_account:
    def __init__(self, interest_rate, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            self.balance - 5
            print("insufficient funds: charging a $5 fee")

    def display_account_info(self):
        print(f"Account Balance is {self.balance}")
    
    def yield_interest(self, interest_rate):
        if self.balance > 0:
            self.balance = self.balance*interest_rate
    