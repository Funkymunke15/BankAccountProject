##This is the BankAccount Module that contains both the BankAccount and Financial classes

class Financial:

    @staticmethod
    def percentOf(sBalance, sInterestRate):
        return sBalance * sInterestRate


class BankAccount:
    _lastAccNum = 1000

    def __init__(self, accName='', balance=0.00, accType='', interestRate=0.03):
        self._balance = balance
        self._accName = accName
        BankAccount._lastAccNum += 1
        self._accNum = BankAccount._lastAccNum
        self._accType = accType
        self._interestRate = interestRate

    def getName(self):
        return self._accName

    def getBalance(self):
        return self._balance

    def getAccType(self):
        return self._accType

    def getAccNum(self):
        return self._accNum

    def withdraw(self, withdrawAmt):
        try:
            if self._balance >= withdrawAmt:
                self._balance -= withdrawAmt
                print(f"{self._accName}'s balance after withdrawal is ${self._balance:.2f}")
            else:
                raise ValueError
        except ValueError:
            return print(f'{self._accName} has insufficient funds')

    def deposit(self, depositAmt):
        self._balance += depositAmt
        print(f"{self._accName}'s balance after deposit is ${self._balance:.2f}")

    def transfer(self, transferAmt, otherAcc):
        try:
            if self._balance >= transferAmt:
                otherAcc._balance += transferAmt
                self._balance -= transferAmt
                print(f"{otherAcc._accName}'s account balance after transfer is ${otherAcc._balance:.2f}")
                print(f"{self._accName}'s account balance after transfer is ${self._balance:.2f}")
            else:
                raise ValueError
        except ValueError:
            return print(f'{self._accName} has insufficient funds')

    def addInterest(self):
        self._balance += self._balance * self._interestRate

    def displayAccountInfo(self):
        print(f'The account name: {self._accName}')
        print(f'The account num: {self._accNum}')
        print(f'The account type: {self._accType}')
        print(f'The account balance: ${self._balance:.2f}')
