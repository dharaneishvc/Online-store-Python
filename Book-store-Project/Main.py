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

    @classmethod
    def checkusername(cls, arr, username):
        for i in arr:
            if(i.username == username):
                return False
        return True   

    @classmethod
    def retcount(cls):
        return User.Count
   

class Seller(User):
    Count = 0
    def __init__(self, username, password, publ):
        User.__init__(username, password)
        self.publ = publ
        Seller.Count += 1
        self.books=[]

    def getpubl(self):
        return self.publ

    def setpubl(self, publ):
        self.publ = publ

    @classmethod        
    def retcount(cls):
        return Seller.Count

    def myprods(self, id):
        self.books.append(id)

    def diplay(self):
        print("UserName: " + self.__username)
        print("Publication: " + self.publ)
        print("Mobile: " + self.mobile)
        print("Email: " + self.mail)
        print("My Books (IDs): " + self.books)

class Customer(User):
    Count = 0
    def __init__(self, username, password, name):
        User.__init__(username, password)
        self.name = name
        Seller.Count += 1
        self.cart=[]

    def getname(self):
        return self.name

    def setname(self, pub):
        self.name = pub

    @classmethod
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
        print("Name: " + self.name)
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

    @classmethod
    def checkpid(cls, arr, pid):
        for i in arr:
            if(i.pid == pid):
                return False
        return True

    def getid(self):
        return self.pid

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
        if(count <= self.stock):
            self.stock -= count
            return True
        else:
            return False

    @classmethod
    def retcount(cls):
        return Books.Count


class Paperbank(Books):
    Count = 0
    def __init__(self, pid, stock, sid):
        Books.__init__(pid, stock, sid)
        Paperbank.Count += 1
    
    def setvalues(self):
        self.name = input("Enter name of the book:")
        self.subj = input("Enter subject of the book:") 
        self.lang = input("enter language of the book:")
        self.auth = input("enter author of the book:")
        self.cost = float(input("Enter cost of the book:"))
        self.weightgms = int(input("Enter Weight of Book(in gms):"))
        self.pages = int(input("Enter Total No of Pages(int): "))

    @classmethod
    def retcount(cls):
        return Paperbank.Count

    def display(self):
        print("P ID: "+ self.pid)
        print("Stock left: "+ self.stock)
        print("Name: "+ self.name)
        print("Language: "+ self.lang)
        print("Subject: "+ self.subj)
        print("Author: "+ self.auth)
        print("Cost(in INR)" + self.cost)
        print("Weight in Gms: "+ self.weightgms)
        print("Total No of pagaes: "+ self.pages)

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

    @classmethod
    def retcount(cls):
        return Ebook.Count

    def display(self):
        print("P ID: "+ self.pid)
        print("Stock left: "+ self.stock)
        print("Name: "+ self.name)
        print("Language: "+ self.lang)
        print("Subject: "+ self.subj)
        print("Author: "+ self.auth)
        print("Cost(in INR)" + self.cost)
        print("File Size in MB: "+ self.filesize)
        print("Total No of pagaes: "+ self.pages)



def custlogin():
    s = 0
    uname = input("Enter Username:")
    pwd = input("Enter Password")
    for i in Customers:
        if(i.login(uname,pwd)):
            print("Log In Sucessfull")
            s=1
            break
    if(s==0):
        print("Log In Unsucessfull. Try gain. Return to main menu")
    else:
        c = 0
        while(c != 5):
            print("1. See Books \n2. Make Purchase \n3. View Details \n4. Edit Details and Reset Password \n5. Exit")
            c = int(input())
            while (i>5 or i<1):
                c = int(input("Error! Enter No: "))
            if(c==1):
                print("Paperbanks:")
                for q in Paperbanks:
                    print("---------------------------------------");
                    q.display()
                print("--------------THE END-------------------");
                print("Ebooks:")
                for q in Ebooks:
                    print("---------------------------------------");
                    q.display()
                print("--------------THE END-------------------");

            elif(c==2):
                id = int(input("Enter P ID: "))
                cnt = int(input("Enter Count: "))
                s=0
                for q in Paperbanks:
                    if q.getid == id :
                        if(q.purchase(cnt)):
                            i.purchase(id,cnt)
                            print("Purchase made successful")
                            s=1
                            break
                        else:
                            print("Count you entered is more than Stock Available")
                if s==0 :
                    for q in Ebooks:
                        if q.getid == id :
                            if(q.purchase(cnt)):
                                i.purchase(id,cnt)
                                print("Purchase made successful")
                                s=1
                                break
                            else:
                                print("Count you entered is more than Stock Available")
                if s==0:
                    print("Product for the product ID is not Found")
            elif(c==3):
                i.display()
            elif(c==4):
                pass
                #GET AND SET OF EACH FUNCTIONS, RESET PASSWORD
            else:
                print("Exiting to Main")
                    


def selllogin(): 
    s = 0
    uname = input("Enter Username:")
    pwd = input("Enter Password")
    for i in Sellers:
        if(i.login(uname,pwd)):
            print("Log In Sucessfull")
            s=1
            break
    if(s==0):
        print("Log In Unsucessfull. Try gain. Return to main menu")
    else:
        c = 0
        while(c != 6):
            print("1. See Books \n2. Add Books \n3. Edit Book Info \n4. View Details \n5. Edit Details and Reset Password \n6. Exit")
            c = int(input())
            while (i>6 or i<1):
                c = int(input("Error! Enter No: "))
            if(c==1):
                print("Paperbanks:")
                for q in Paperbanks:
                    print("---------------------------------------");
                    q.display()
                print("--------------THE END-------------------");
                print("Ebooks:")
                for q in Ebooks:
                    print("---------------------------------------");
                    q.display()
                print("--------------THE END-------------------");

            elif(c==2):
                id = int(input("Enter P ID: "))
                if(Books.checkpid(Paperbanks, id) and Books.checkpid(Ebooks,id)):
                    c = int(input("1 PaperBank \n 2 Ebook \n 3 Exit \n Enter: "))
                    while(c!=1 or c!=2 or c!=3):
                        c=int(input("Error. Enter again(1-3): "))
                    if(c==1):
                        stock = int(input("Enter stock size: "))
                        temp = Paperbank(id,stock,i.getid())
                        temp.setvalues
                        Paperbank.append(temp)
                        print("Book added succesfully")
                    elif(c==2):
                        stock = int(input("Enter stock size: "))
                        temp = Ebooks(id,stock,i.getid())
                        temp.setvalues
                        Paperbank.append(temp)
                        print("Book added succesfully")
                    else:
                        print("Book Not added!")
                else:
                    print("ID is unavailable. Try Again")

            elif(c==3):
                pass
            #GET AND SET FUNCTIONS IN BOOK
        
                
                if s==0:
                    print("Product for the product ID is not Found")
            elif(c==4):
                i.display()
            elif(c==5):
                pass
                #GET AND SET OF EACH FUNCTIONS, RESET PASSWORD
            else:
                print("Exiting to Main")

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
        custlogin()
    elif c==2 :
        selllogin()

    elif c==3:
        uid = input("Enter a unique User ID")
        if(User.checkusername(Sellers, uid) and User.checkusername(Customers, uid)):
            pass1 = input("Enter Password: ")
            if(pass1==input("Re-enter Password:")):
                name = input("Enter Name")
                temp = Customer(uid, pass1, name)
                Customers.append(temp);
                print("User ID created. Log in and add your mobile, email")
        else:
            print("Username unavailable")
         

    elif c==4:
        uid = input("Enter a unique User ID")
        if(User.checkusername(Sellers, uid) and User.checkusername(Customers, uid)):
            pass1 = input("Enter Password: ")
            if(pass1==input("Re-enter Password:")):
                publ = input("Enter Publication Name:")
                temp = Seller(uid, pass1, publ)
                Sellers.append(temp);
                print("User ID created. Log in and add your mobile, email")
        else:
            print("Username unavailable")

    else:
        print("Thank You for using this product")

