# each class have the
class computer:
    # propioties
    # the constructor : is an inisialization of anobject : (give an spase of the object in the momary )
    # this not important so we can not use it because python have the default one 
    def __new__(cls,*argm):
        instance = super().__new__(cls)
        return instance
    

        
    # this how create a init method 
    def __init__(self,cpu,ram,storage,brand):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.brand = brand
    # 

    # method 
    def display(self):
        print("\n")
        print("*"*80)
        print("the confgrution of the computer : \n")
        print("the CPU of the computer is : ",self.cpu)        
        print("the RAM of the computer is : ",self.ram ,'GB')
        print("the STORAGE of the computer is : ",self.storage , 'GB')
        print("the BRAND of the computer is : ",self.brand )
        print("*"*80)
# fonction to enter the confguration of the pc 
def create_pc():
    cpu = input("enter the  ( CPU ) of your pc : ")
    ram = input("enter the ( RAM ) of your pc : ")
    storage = input("enter the ( STORAGE ) of your pc : ")
    brand = input("enter the ( BRAND ) of your pc : ")
    return computer(cpu,ram,storage,brand)
pc1 = create_pc()
pc1.display()