# we have three type of method 
    # instance method : like all method take self as a parematers like init method
    # class method : take cls as a parameters like new method
    # static method : dont take no (self or  cls)
# THE DECORATOR : is change what the python send first as a default parameters  
class computer:
    total = 0 # its an atrebiute
    # exp : instance 
    def __init__(self,cpu,ram,storage,brand):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.brand = brand
    # exp :  class method
    # also we need do the [ decorator ]
    @classmethod
    def get_totly(cls):
        return "total is :",cls.total
         
    def display(self):
            print("\n")
            print("*"*80)
            print("the confgrution of the computer : \n")
            print("the CPU of the computer is : ",self.cpu)        
            print("the RAM of the computer is : ",self.ram ,'GB')
            print("the STORAGE of the computer is : ",self.storage , 'GB')
            print("the BRAND of the computer is : ",self.brand )
            print("*"*80)
    
    @staticmethod
    def is_valid_size(size):   # static method
        return size in ("32", "43", "50", "55", "60", "65")

print(computer.is_valid_size("50"))   # True
print(computer.is_valid_size("999"))  # False