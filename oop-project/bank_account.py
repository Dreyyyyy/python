class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.accName = accName
        print(f"\nAccount '{self.accName}' created.\nBalance: ${self.balance:.2f}.\n")

    def getBalance(self):
        print(f"Account '{self.accName}' balance: ${self.balance:.2f}\n")

    def deposit(self, amount):
        self.balance += amount

        print("\nDeposit complete.")

        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account '{self.accName}' only has a balance of ${self.balance:.2f}."
            )

    def withdraw(self, amount):
        try:
            print("\n**********Beggining transfer...")
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransference completed.**********")
        except BalanceException as error:
            print(f"\nTransference interrupted: {error}**********")


class InterestRewardAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAcc(InterestRewardAcc):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount + self.fee
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print("Withdraw interrupted: {error}")
