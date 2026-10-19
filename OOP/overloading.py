# POLYMORPHISM : The ability of an object to take many forms.
    # also : the same name or operation behaves differently depending on the situation.
# In Python, polymorphism is achieved through method overriding and method overloading.
#  ( in C++ an java do the overloading direactly but in python we can do it by default )
# 1 \ methode overloading : 
    # Operator overloading means you teach Python what an operator like + 
    # does for your own class.
    # Python knows 2 + 3, but it doesn’t know what account1 + account2 means. 
    # So you write a special method called __add__, and Python calls it every time it sees + between your objects.”

class Account:
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance

    # for print the objectfor return a string 
    def __str__(self):
        return f"{self.name} : {self.balance}"

    # for adding two objects of the same class
    def __add__(self ,you ):
        # we put the result in new object and return it
        return Account("combaine ",self.balance + you.balance)
    
    # for compare between tow object we use __gt__ 
    def __gt__(self,you):
        return self.balance > you.balance
    # for greater than and __lt__ for less than
    def __lt__(self,you):
        return self.balance < you.balance

    # for compare between tow object we use __eq__ for equal than
    def __eq__(self,you):
        return self.balance == you.balance

    # for get the length of the object we use __len__
    def __len__(self):
        return len(self.name)
    


user1 = Account("moha",1000)
user2 = Account("ali",1244)

comination = user1 + user2
print(comination)    
if user1 > user2  :
    print(f"{user1.name} will pay ")
else :
    print(f"{user2.name} will pay")
    




