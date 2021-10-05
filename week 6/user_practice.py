class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
    
    def withdrawl(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"my name is {self.name} and my account balance is {self.account_balance}")
    
    def transfer_money(self,transferring_to, amount):
        transferring_to.account_balance += amount
        self.account_balance -= amount
        print({f"{self.name} transferred {amount} to {transferring_to.name}"})


raphael = User('rapahel', 'hello@email.com')
raphael.make_deposit(500)
raphael.withdrawl(75)
print(raphael.account_balance)
raphael.display_user_balance()

jenny = User('jenny', 'itsmejen@email.com')
jenny.make_deposit(100)
print(raphael.account_balance)
print(jenny.account_balance)

jenny.transfer_money(raphael,25)
print(raphael.account_balance)
print(jenny.account_balance)





