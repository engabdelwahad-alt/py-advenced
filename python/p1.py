
class computer:
    # propioties
    def __init__(self,cpu,ram,storage,brand,type,gpu = 'NON'):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.brand = brand
        self.type = type
        self.gpu = gpu

    # method 
    def dispaly(self):
        print("the confgrution of the computer : \n")
        print("the CPU of the computer is : ",self.cpu)        
        print("the RAM of the computer is : ",self.ram ,'GB')
        print("the STORAGE of the computer is : ",self.storage , 'GB')
        print("the BRAND of the computer is : ",self.brand )
        print("the  TYPE of the computer is : ",self.type)
        print("the GPU  of the computer is : ",self.gpu)

# fonction to enter the confguration of the pc 
def create_pc():
    cpu = input("enter the  ( CPU ) of your pc : ")
    ram = input("enter the ( RAM ) of your pc : ")
    storage = input("enter the ( STORAGE ) of your pc : ")
    brand = input("enter the ( BRAND ) of your pc : ")
    type = input("enter the ( TYPE ) of your pc : ")
    gpu = input("enter the ( GPU ) of your pc or if you don't have press enter : ")

    if not gpu:
        gpu = "i dont have a gpu"
    return computer(cpu,ram,storage,brand,type,gpu)

    def games():
        
        # cheack the cpu 
        # ram
        # storage 
        # 
        pass
    def programing():
        pass
    def simple():
        pass






def search():
    pass











# pc1 = create_pc()
# pc1.dispaly()

