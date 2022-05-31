from abc import ABC, abstractmethod


class User(ABC):  # declaring a parent class of User
    def __init__(self, name, password):
        self.name = name
        self.__password = password  # hidden attribute password

    def get_password(self):
        return self.__password

    def __getitem__(self, i):  # to make the class subscript-able
        return f"Value {i}"

    @abstractmethod  # declaring an abstract method as the other children classes would have different attributes
    def __repr__(self):
        return f"Name: {self.name}, Password: {self.get_password()}"


class Lender(User):  # defining a lender class with name and rate attributes
    def __init__(self, name, password, rate):
        super().__init__(name, password)
        self.__rate = rate  # encapsulating the rate so that it is not modifiable by user
        self.total = 0
        self.borrowers = []  # list of all borrowers

    def get_rate(self):
        return self.__rate

    def get_borrowers(self):
        for e in self.borrowers:
            yield (e, '\n')

    def __repr__(self):
        return f"Name: {self.name}, Rate: {self.get_rate()}%, Total money to be paid to user : {self.total}, Borrowers: {self.borrowers} "


class Borrower(User):  # defining a borrower class with name amount and time attributes
    def __init__(self, name, password):
        super().__init__(name, password)
        self.amount = None
        self.time = None
        self.sum = None
        self.lenders = []

    def get_lenders(self):
        for e in self.lenders:
            yield (e, '\n')

    def __repr__(self):
        return f"Name: {self.name}, Total money owed: {self.sum}, Lender: {self.get_lenders()}"


def loan(b, l):  # calculating the loan for specific lender
    b.sum = b.amount * (pow((1 + l.get_rate() / 100), b.time))
    l.total += b.sum
    print(b.name, " owes ", l.name, b.sum, "over the course of", b.time, "years")


def payback(b, l, x):  # if borrower wants to payback a lender
    b.sum -= x
    l.total -= x
    print(b.name, " owes ", l.name, b.sum)


# declaring two lists which will store the objects of Lender and Borrower classes

llist = []
blist = []


def addlendor():  # adding an object in list of lenders
    name = input("Enter name of lendor:\n")
    pwd = input("Enter your password\n")
    rate = float(input("Enter the rate at which they lend p.a.:\n"))
    llist.append(Lender(name, pwd, rate))


def addborrower():  # adding an object in list of borrowers
    name = input("Enter name of borrower:\n")
    pwd = input("Enter  your password\n")
    blist.append(Borrower(name, pwd))


def blogin():  # login for borrower
    name = input("Enter your name\n")
    pwd = input("Enter your password\n")
    c = False
    for i in blist:
        if i.name == name and i.get_password() == pwd:  # checking for password
            bpage(i)
            c = True
        else:
            continue
    if c is False:
        print("Check login ID or create new account")


def bpage(i):  # page for borrower
    print("1.New loan\n2.Pay existing loan\n3.My details\n4.Exit\n")
    c = int(input())
    if c == 1:
        f = 1
        for e in llist:
            print(f, " lender:", i.name, "Rate p.a.", e.get_rate(), '%\n')  # prints all lenders values
            f += 1
        j = int(input("which lender do u wanna loan from? (enter serial number)\n")) - 1
        i.amount = float(input("Enter the amount you want to loan:"))
        i.time = int(input("Enter the time you  want the loan for:"))
        loan(i, llist[j])
        i.lenders.append([llist[j].name, i.sum])  # appending into the borrower user
        llist[j].borrowers.append([i.name, i.sum])  # appending into the lender user
        bpage(i)
    elif c == 2:
        f = 0
        for e in i.lenders:
            f += 1
            print(f, " ", e)
        j = int(input("which lender do payback (enter serial number)\n")) - 1
        amt = float(input("Enter amount to be paid back"))
        payback(i, llist[j], amt)  # for paying back specific lenders
        bpage(i)
    elif c == 3:
        print(i)
        bpage(i)
    else:
        main()


def llogin():  # login  for lender
    name = input("Enter your name\n")
    pwd = input("Enter your password\n")
    c = False
    for i in llist:
        if i.name == name and i.get_password() == pwd:  # checking for password
            lpage(i)
            c = True
        else:
            pass
    if c is False:
        print("Check login ID or create new account")


def lpage(i):  # pagee for lender
    print("1.Check loan status\n2.Show details\n3.Quit")
    c = int(input())
    if c == 1:
        print(f"Total money to be paid back: {i.total}")
        for e in i.borrowers:
            print(e)
        lpage(i)
    elif c == 2:
        print(i)
        lpage(i)
    else:
        main()


def main():
    print('1. Borrower \n2. Lender\n3. Quit')
    c1 = int(input())
    if c1 == 1:  # borrowers1
        print("1. New \n2. Existing")
        c2 = int(input())
        if c2 == 1:
            addborrower()
            main()
        elif c2 == 2:
            blogin()
        else:
            print("Enter valid option")
            main()

    elif c1 == 2:  # Lenders
        print("1. New \n2. Existing")
        c3 = int(input())
        if c3 == 1:
            addlendor()
            main()
        elif c3 == 2:
            llogin()
        else:
            print("Enter valid option")
            main()
    elif c1 == 3:
        quit()
    else:
        print("Enter valid option")
        main()


main()
