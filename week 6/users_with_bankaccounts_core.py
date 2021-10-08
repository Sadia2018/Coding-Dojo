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

# user class
class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = bank_account(interest_rate = 0.00, balance = 0)
        # self.account_balance = 0

    def make_deposit(self,amount):
        # self.account_balance += amount
        # bank_account.balance += amount
        self.account.deposit(amount)

    def withdrawl(self, amount):
        # self.account_balance -= amount
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f"my name is {self.name} and my account balance is {self.account.balance}")
    
    def transfer_money(self,transferring_to, amount):
        transferring_to.account_balance += amount
        self.account_balance -= amount
        print({f"{self.name} transferred {amount} to {transferring_to.name}"})




raphael = User('raphael', 'rk@email.com')
raphael.make_deposit(1000)
raphael.display_user_balance()


# checking_account = bank_account(0.03)
# investment_account = bank_account(0.05)
# retirement_account = bank_account(0.03)

# bank_account.all_instances()


# checking_account.deposit(1000).deposit(1000).deposit(1000).withdraw(50).yield_interest(0.03).display_account_info()

# investment_account.deposit(1000).withdraw(1000).withdraw(1000)