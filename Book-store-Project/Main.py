class User:
    Count = 0
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        User.Count+=1

    def setmail(self, mail):
        self.mail = mail

    def setmobile(self, mobile):
        self.mobile = mobile

    def getmail(self):
        return self.mail

    def getmobile(self):
        return self.mobile

    def login(self, uname, pwd):
        if(self.__username == uname and self.__password == pwd):
            return 1
        else:
            return 0

    def resetpass(self):
        if(self.__password == input("Enter Old Paswword")):
            np = input("Enter New Password")
            if( np == input("Confirm Re-enter Password")):
                self.__password = np
                print("Password Changed Succesfully")
            else:
                print("Password doesn't match. Try Again.")
        else:
            print("Wrong Password. Try again.")

    def checkusername(cls, arr, username):
        for i in arr:
            if(i.username == username):
                return False
        return True   

    def retcount(cls):
        return User.Count
   

class Seller(User):
    Count = 0
    def __init__(self, username, password, name):
        User.__init__(username, password)
        self.name = name
        Seller.Count += 1
        self.books=[]

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name
            
    def retcount(cls):
        return Seller.Count

    def myprods(self, id):
        self.books.append(id)

    def diplay(self):
        print("UserName: " + self.__username)
        print("Name: " + self.name)
        print("Mobile: " + self.mobile)
        print("Email: " + self.mail)
        print("My Books (IDs): " + self.books)

class Customer(User):
    Count = 0
    def __init__(self, username, password, publication):
        User.__init__(username, password)
        self.publication = publication
        Seller.Count += 1
        self.cart=[]

    def getpublication(self):
        return self.publication

    def setpublication(self, pub):
        self.publication = pub

    def retcount(cls):
        return Customer.Count

    def purchase(self, pid, count):
        for i in self.cart:
            if(i["pid"] == pid):
                i["count"] += count
                return
        mydict = {"pid":pid, "count":count}
        self.cart.append(mydict)

    def diplay(self):
        print("UserName: " + self.__username)
        print("Publication: " + self.publication)
        print("Mobile: " + self.mobile)
        print("Email: " + self.mail)
        print("My Cart (PID, Count): " + self.cart)


    
class Books:
    Count = 0
    def __init__(self, pid, stock, sid):
        self.pid = pid
        self.stock = stock
        self.seller = sid
        Books.Count += 1

    def checkpid(cls, arr, pid):
        for i in arr:
            if(i.pid == pid):
                return False
        return True

    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name

    def setsubj(self, subj):
        self.subj = subj
    
    def getname(self):
        return self.subj

    def setlang(self, lang):
        self.lang = lang
    
    def getlang(self):
        return self.lang

    def setauth(self, auth):
        self.auth = auth
    
    def getauth(self):
        return self.auth

    def setcost(self, cost):
        self.cost = cost
    
    def getcost(self):
        return self.cost

    def setpages(self, page):
        self.pages = page

    def getpages(self):
        return self.pages

    def setseller(self, sell):
        self.seller = sell

    def purchase(self, count):
        self.stock -= count

    def retcount(cls):
        return Books.Count

class Paperbank(Books):
    Count = 0
    def __init__(self, pid, stock, sid):
        Books.__init__(pid, stock, sid)
        Paperbank.Count += 1
    
    def setvalues(self):
        self.name = input("Enter name of the book:")
        self.lang = input("Enter subject of the book:") 
        self.lang = input("enter language of the book:")
        self.auth = input("enter author of the book:")
        self.cost = float(input("Enter cost of the book:"))
        self.weightgms = int(input("Enter Weight of Book(in gms):"))
        self.pages = int(input("Enter Total No of Pages(int): "))

    def retcount(cls):
        return Paperbank.Count

class Ebook(Books):
    Count = 0
    def __init__(self, pid, stock, sid):
        Books.__init__(pid, stock, sid)
        Ebook.Count += 1
    
    def setvalues(self):
        self.name = input("Enter name of the book:")
        self.lang = input("Enter subject of the book:") 
        self.lang = input("enter language of the book:")
        self.auth = input("enter author of the book:")
        self.cost = float(input("Enter cost of the book:"))
        self.filesize = float(input("Enter File Size of PDF(in megabytles):"))
        self.pages = int(input("Enter Total No of Pages(int): "))

    def retcount(cls):
        return Ebook.Count


print("WELCOME TO BOOK STORE")
c = 0
Sellers = []
Customers = []
Paperbanks = []
Ebooks = []


while(c != 5):
    print("1. Customer Log In \n 2. Seller Log In \n 3. Customer Sign Up \n 4. Seller Sign Up \n 5.Exit \nEnter:")
    c = int(input())
    while (c>5  or c<1):
        c = int(input("Error! Enter value(1-4):"))
    if c==1 :
        s = 0
        uname = input("Enter Username:")
        pwd = input("Enter Password")
        for i in Customers:
            if(i.login(uname,pwd)):
                print("Log In Sucessfull")
                s=1
                break
        if(s==0):
            print("Log In Unsucessfull")
        else:


    elif c==2 :

    elif c==3:

    elif c==4:

    else:
        print("Thank You for using this product")

