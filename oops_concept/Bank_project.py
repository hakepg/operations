import sys
class Customer:
    CBank = 'SBI'
    def __init__(self,name,balance=0):
        self.custName = name
        self.custBal=balance

    def deposit(self,amt):
        deposit = self.custBal+amt
        print('the balance after deposit is:',deposit)


    def withdrow(self,amt):
        if amt>self.custBal:
            print('insufficient balanace..cannot withraw')
        self.custBal = self.custBal-amt
        print('after withdraw balance is:',self.custBal)
        sys.exit()

print('Welcome to the ',Customer.CBank)
name = input('Enter your name:')
c = Customer(name)
while True:
    print('d = Deposit\nw=Withdraw\ne=Exit\n')
    option = input('enter the option:')
    if option=='d' or option=='D':
        amt = float(input('enter amount to deposit:'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt = float(input('enter amount to withdraw:'))
        c.withdrow(amt)
    elif option=='e' or option=='E':
        print('thanks for banking with {}'.format(Customer.CBank))
        sys.exit()

    else:
        print('choose valid option')


