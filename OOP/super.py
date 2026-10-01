class A():
    def __init__(self):
        print('work in the  A')

    def f1(self):
        print(" A ")
class B(A):

    def __init__(self):
        #  if we want to print both of the init of the super and sub calss so we use super method 
        super().__init__()
        print("work in the B")
            # they print it both a and b 
    
    def f2(self):
        self.f1()
        # also we can use super here
        # super().f1()
        print(" B ")
#  NOTE :  if you want the best option use [ super ]
    # super go directly to the super class and skip the subclass so we dont have any error with that 
    # but when we have [self] cheak first the subclass the if dont find it go to the super class 
        #  when we have tow method with the same name this a error if we use this because is still in the subclass and work as a loop 
            # infinite recrusion 
        


c1 = B()
# init in python its call itself so we dont need to call it again okay 
    # its work automatecly when we create the object 
# c1.__init__()

c1.f2()
