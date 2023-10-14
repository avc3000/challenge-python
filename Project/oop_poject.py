from bank_account import *

Antony = BankAccount(1000, "Antony")
Sara = BankAccount(2000, "Sara")

Antony.getBalance()
Sara.getBalance()

Sara.deposit(500)

Antony.withdraw(10000)
Antony.withdraw(10)

Antony.transfer(10000, Sara)
Antony.transfer(10, Sara)

Jim = InterestRewardAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Antony)

Blaze = SavingsAccount(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Antony)