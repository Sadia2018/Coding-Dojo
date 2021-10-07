class bank_account:
    # class attribute
    all_accounts = []
    # instance attributes
    def __init__(self, interest_rate, balance = 0):
        self.interest_rate = interest_rate
        self.balance = balance
        bank_account.all_accounts.append(self)

    #instance methods
    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            self.balance - 5
            print("insufficient funds: charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Account Balance is {self.balance}")
        return self
    
    def yield_interest(self, interest_rate):
        if self.balance > 0:
            self.balance += self.balance*interest_rate
        return self

    #class method
    @classmethod
    def all_instances(cls):
        for x in cls.all_accounts:
            x.display_account_info()

checking_account = bank_account(0.03)
investment_account = bank_account(0.05)
retirement_account = bank_account(0.03)

bank_account.all_instances()


checking_account.deposit(1000).deposit(1000).deposit(1000).withdraw(50).yield_interest(0.03).display_account_info()

investment_account.deposit(1000).withdraw(1000).withdraw(1000)