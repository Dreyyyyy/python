from bank_account import *

dave = BankAccount(1000, "Dave")
sarah = BankAccount(2000, "Sarah")

dave.getBalance()
sarah.getBalance()

dave.deposit(570)
sarah.deposit(322)

dave.withdraw(216)
sarah.withdraw(620)

dave.withdraw(100000)

sarah.transfer(100000, dave)
sarah.transfer(231, dave)

jim = InterestRewardAcc(1000, "Jim")

jim.getBalance()

jim.deposit(100)

jim.transfer(100, dave)

joanne = SavingsAcc(1000, "Joanne")

joanne.getBalance()

joanne.deposit(100)

joanne.transfer(3000, sarah)
