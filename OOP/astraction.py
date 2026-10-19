# ABSTRACT  : ITS LIKE HIDING THE DETAILS AND SHOWING ONLY WHAT METTERS
# (what somthing does not how it does it )
#  NOTE : 
    # in python we can achieve abstraction by using abstract classes and methods from the abc module.
# we will import ABC class and the abstractmethod (method) form the abc module
from abc import ABC,abstractmethod
# we must be inherited A form class ABC to make it abstract class
# (A extends from ABC )
class A(ABC):
    def __init__(self,name,age):
            self.name = name
            self.age = age
    # also we must use the @abstractmethod decorator to make the method abstract
        #  now any class that inherits from A must implement the show method or it will raise an error
    @abstractmethod
    def show(self,me):
        me = print("this is abstract method")
        return me
class B(A):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name : {self.name}")
        print(f"age : {self.age }")
        
    def show(self):
        self.display()

c1 = B("ahmed",21)
c1.show()

#  this does not work because we can't instantiate an abstract class
c2 = A("alice", 25)    #TypeError: Can't instantiate abstract class A without an implementation for abstract method 'show'
c2.show()












