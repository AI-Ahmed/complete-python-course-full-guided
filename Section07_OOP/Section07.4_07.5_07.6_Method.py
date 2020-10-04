__author__ = "crypto"
# Method Part 1
import datetime
import pytz

"""
One of the important aspects in OOP is Encapsulation:
           The idea here is that objects contain the data and the methods
           that operate on that data and don't expose the actual implementation 
           to the outside world.
"""


class Account:
    """ Simple account class with balance"""

    @staticmethod
    def _current_time():  # using underscore before the method name indicate anyone using this code that this method isn't a normal method usage of the class
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._transaction_list = [(Account._current_time(),
                                   balance)]  # we will add the transaction amount and date into a list, so we can configure each transaction and its date
        # self._balance = balance  # you must to consider that the attribute whose name start with single underscore are for 'internal use' ONLY
        self.__balance = balance  # with double underscore it will work. self.__balance is the instance attribute equivalent to the constructor
        print("Account created for " + self._name)
        # self.transaction_list.append((Account._current_time(), self.balance))   # you can use this or you can initially add the balance and the _current_time into the list itself
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            # for more realistic, let's add print method to show the balance after the deposit
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))   # we created the transaction list to contain tuples so we can assign a value with several variables in a single assignment statement by using a tuple
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # this will prevent withdraw by -, which means over the account's balance
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, trans_type, date, date.astimezone()))


# =======================================================
# create account for myself :D


if __name__ == '__main__':
    crypto = Account("Crypto", 0)
    crypto.show_balance()

    crypto.deposit(500)
    # crypto.show_balance()
    crypto.withdraw(25)
    # crypto.show_balance()

    # lets try now to withdraw more than the balance
    crypto.withdraw(1000)
    # **********************************************************************************************
    # Method Part 2

    # Like we mentioned into the last session, there's a technical issue related to the transaction
    # we need to add date and time to these transaction

    crypto.show_transaction()
# what happens here that Python unpack the tuple in the for loop instead of just assigning a value to a single variable
#

"""
like we've done in the deposit method, we need to do the same thing into the withdraw method
but if you notice that better than duplicate the code we can create a method that can be accessed by any other method
in OOP called 'Static method' which the same term used in java or c++ 

Static method: is shared by all instance of the class in the same way that the 'power_source' class attribute of our Kettle class was shared
by all instances so making the method static is pretty simple by remove 'self' and add annotation @staticmethod

One of the  notice: 
you can use self._current_time() as you can use Account._current_time() BUT it will sightly suffers and that's because 
Python will attempts to find the method in the instances namespace and when it can't find it it will search in class namespaces
so, its better to directly mention it Class._staticmethod()
"""

# **********************************************************************************************

# Non Public and Mangling

if __name__ == '__main__':
    tim = Account("Tim", 800)  # if you notice the method hasn't taken the initial deposit into account
    # lets try to initialise a variable with the same name of the attribute of the constructor
    tim.__balance = 200
    # tim.balance = 200 # both works, python mangled the attribute
    tim.deposit(100)
    tim.withdraw(200)
    tim.show_transaction()
    tim.show_balance()
    # so, the value of the object has been changed because the instance 'tim' has an attribute with the class variable name
    # and this will affect badly on the variables' value. Now we need to refactor the constructor's variables name
    # another thing being highlighted that the variables with double underscore intended for use when subclassing
    # the idea to prevent the name clashes.
    #
    # lets print the namespace of our new account to see what's going on and why _balance with single underscore didn't work
    print(tim.__dict__)

    # so, first tim's attribute has called __balance with a $200. now this data attribute was created when we assign the value of 200
    # python didn't find an attribute with that name in steps namespace so it looked at the class' namespace and didn't find it there either
    # and that's a result to create new data attribute <same condition of power attribute>

    # second reason why python didn't find balance at the beginning that there's data attribute called '_Account__balance'
    # some by prefixing the name balanced with two underscores we're asking python to perform name mangling and it automatically renames
    # the attributes to start with an underscore and the name of the classes as you can see and this's done behind the scene our source
    #  code isn't changed.

    # but if you want to change the mangling that python had changed <not recommended> :
    # tim._Account__balance = 48
    # tim.show_balance()
