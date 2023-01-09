class Bank():
    def __init__(self,account_number):
        account_number = str(account_number).replace(' ', '')
        self.acc_no = account_number
        self.acc_balance = 0

    def status(self):
        print('Bank Account No: ',end='')
        for a in range(26):
            if a in [1,5,9,13,17,12]:
               print(self.acc_no[a], end=" ") 
            else:
                print(self.acc_no[a], end="")

        print(f'\nBalance: PLN {self.acc_balance}')

    def deposit(self,amount):
        '''Adds funds to balance'''
        self.acc_balance += amount


    def withdraw(self,amount):
        if amount <= self.acc_balance:
            self.acc_balance -= amount
        else:
            print('Insufficient funds on the account')

   


maciek = Bank(12345655559090111100007722)
maciek.status()
maciek.deposit(25.30)
maciek.status()
maciek.withdraw(31.70)
maciek.status()
maciek.withdraw(14)
maciek.status()