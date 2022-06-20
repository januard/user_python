class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

adrien = User("Adrien")
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")

adrien.make_deposit(150)
adrien.make_deposit(500)
adrien.make_deposit(50)
adrien.make_withdrawl(45)
adrien.display_user_balance()

nibbles.make_deposit(2000)
nibbles.make_deposit(1000)
nibbles.make_withdrawl(200)
nibbles.make_withdrawl(300)
nibbles.display_user_balance()

benny_bob.make_deposit(1300)
benny_bob.make_withdrawl(1000)
benny_bob.make_withdrawl(2000)
benny_bob.make_withdrawl(2000)
benny_bob.display_user_balance()


nibbles.transfer_money(400, adrien)