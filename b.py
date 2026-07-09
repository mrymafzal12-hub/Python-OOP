from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self, name):
        self.name = name
        self.amount = 100000
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value > 0:
            self.__balance = value

            #print(self.__balance)
        else:
            self.__balance = None

    def deposit(self):
       print(f"Account Holder : {self.name}")
       if self.balance is None:
           print("Invalid Amount !")
       else:
          self.amount = (self.amount + self.balance)
          print(f"Updated Amount  : {self.amount}")


    def withdraw(self):
        print(f"Account Holder : {self.name}")
        if self.balance  is None:
            print("Invalid Amount !")
        else:
           self.amount = (self.amount - self.balance)
           print(f"Remaining Amount : {self.amount}")

    @abstractmethod
    def interest(self):
        print(f"Account Holder : {self.name}")
        pass

class SavingsAccount(BankAccount):
    interest_rate = 5
    def __init__(self,name):
        super().__init__(name)
    def interest(self):
        print(f"Account Holder : {self.name}")
        interest=self.amount * self.interest_rate/100
        print(f"Interest On Current Amount: {interest}")

class CheckingAccount(BankAccount):
    interest_rate = 2
    def __init__(self,name):
        super().__init__(name)
    def interest(self):
        print(f"Account Holder : {self.name}")
        interest=self.amount * self.interest_rate/100
        print(f"Interest On Current Amount : {interest}")

print("----Welcome to Maryam's Bank----")
Name=input("Enter your name: ")
Account_type=input("Which account would you like to check ? : ").lower()
if Account_type=="savings":
        account = SavingsAccount(Name)

elif Account_type == "checking":
       account = CheckingAccount(Name)
else:
     print("Invalid account type")
     exit()
print("1. Withdraw")
print("2. Deposit")
print("3. Interest")
purpose=input("What would you like to do?")

if purpose=="withdraw" :
     amt = int(input("Enter the amount you want to withdraw: "))
     account.balance=amt
     account.withdraw()
elif purpose=="deposit" :
     amt = int(input("Enter the amount you want to deposit: "))
     account.balance=amt
     account.deposit()
elif purpose=="interest":
    account.interest()

