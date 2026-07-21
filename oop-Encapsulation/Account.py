class Account:
    def __init__(self):
        self.__type = None
        self.__number = None
        self.__mode = None
        self.__balance = 0.0

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

    def deposit(self, amt):
        self.__balance = self.__balance + amt
        print("Total balance after deposit:", self.__balance)

        # Withdrawal method

    def withdrawal(self, amt):
        if amt < self.__balance:
            self.__balance = self.__balance - amt
            print("Total balance after withdrawal:", self.__balance)
        else:
            print("Insufficient fund transfer")
a = Account()
a.set_type("active")
a.set_number("998899")
a.set_mode("saving")
a.set_balance(10000)


print("account type =",a.get_type())
print("account number =",a.get_number())
print("account mode =",a.get_mode())
print("account balance =",a.get_balance())

a.deposit(100)
a.withdrawal(100)
