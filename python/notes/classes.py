# ============================================================
# CLASSES - quick reference
# ============================================================


# -- Class = blueprint, object = what you build from it -----
class Account:

    def __init__(self, owner, balance=0):   # constructor, runs at creation
        self.owner = owner                  # attribute of THIS object
        self.balance = balance

    def deposit(self, amount):              # method
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
        else:
            self.balance -= amount

    def show_balance(self):
        print(f'{self.owner}: {self.balance}')


mine = Account('Hippolyte', 200)    # object 1
other = Account('Marie')            # object 2, balance=0 by default

mine.deposit(50)
mine.withdraw(300)    # Insufficient balance
mine.withdraw(100)
mine.show_balance()   # Hippolyte: 150
other.show_balance()  # Marie: 0   (objects are independent)


# -- Key words ----------------------------------------------
# class      defines the class
# __init__   constructor
# self       the object itself: mine.deposit(50) = Account.deposit(mine, 50)
# self.x     attribute: data stored in the object


# -- Function or method? ------------------------------------
# Function: defined outside a class, called as  show(x)
# Method: defined inside a class, called on an object  mine.show_balance()
# A method always takes self as its first parameter


# -- Frequent mistakes --------------------------------------
# def __init__(owner, balance)       -> forgot self
# self.owner = 0                     -> assigned a constant, not the parameter
# def withdraw(self.amount)          -> '.' instead of ','
