from BankAccount import BankAccount

samsAcc = BankAccount('Sam', 100, 'saving')
leilasAcc = BankAccount('Leila', 500, 'saving')
adamsAcc = BankAccount('Adam', 100, 'checking', interestRate=0)

adamsAcc.addInterest()
samsAcc.addInterest()
leilasAcc.addInterest()

print(f'Leila\'s balance after interest is ${leilasAcc.getBalance():.2f}')
print(f'Sam\'s balance after interest is ${samsAcc.getBalance():.2f}')
print(f'Adam\'s balance after interest is ${adamsAcc.getBalance():.2f}')

print()
samsAcc.transfer(200, adamsAcc)

print()
leilasAcc.transfer(50, adamsAcc)

leilasAcc.deposit(100)
samsAcc.deposit(100)
adamsAcc.deposit(100)

print()

adamsAcc.withdraw(300)

print()

leilasAcc.withdraw(200)
samsAcc.withdraw(200)

print(f'{adamsAcc.getName()} account num: {adamsAcc.getAccNum()}')
print(f'{adamsAcc.getName()} account type: {adamsAcc.getAccType()}')

print()

samsAcc.displayAccountInfo()

print()

leilasAcc.displayAccountInfo()

print()

adamsAcc.displayAccountInfo()