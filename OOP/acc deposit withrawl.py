class Account:
    def __init__(self):
        self.__type = None
        self.__number = None
        self.__mode = None
        self.__balance = 0.0
        self.__deposit_count =0

    def set_type(self,type):
        self.__type = type
    def get_type(self):
        return self.__type

    def set_number(self,number):
        self.__number = number
    def get_number(self):
        return self.__number

    def set_mode(self,mode):
        self.__mode = mode
    def get_mode(self):
        return self.__mode

    def set_balance(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

        # Deposit method

    def deposit(self,amt):
       if self.__deposit_count>=5:
           print("ek din m 5 baar se jyada deposit nahi")
       elif amt>50000:
           print("ek baar m 50000 se jyada deposit nahi kar skte")
       elif amt<=0:
           print("invalid amount")
       else:
           self.__balance+=amt
           self.__deposit_count+=1
           print("total balance after deposit:",self.__balance)
           print("deposit count:", self.__deposit_count)



        # Withdrawal method

    def withdraw(self,amount):

        if amount>5000:
            print("ek baar me 5000 se jyada withdraw nahi kar sakte")
            return
        if amount> self.__balance:
            print("insufficient balance")
            return
        self.__balance-=amount
        print("withrwal successful")
        print("current balance:",self.__balance)

a = Account()
a.set_type("active")
a.set_number("998899")
a.set_mode("saving")
a.set_balance(10000)


print("account type =",a.get_type())
print("account number =",a.get_number())
print("account mode =",a.get_mode())
print("account balance =",a.get_balance())

a.deposit(50001)
a.deposit(1)
a.deposit(1)
a.deposit(1)
a.deposit(1)
a.deposit(1)
a.deposit(1)


a.withdraw(5100)
