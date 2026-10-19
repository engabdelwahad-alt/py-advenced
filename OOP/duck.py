# DUCK : Python does not care about the object’s type. It only cares whether the object has the method you call.
    #  its can work without inheritance and super class and sub class
class Laptop:
    def build (self):
        print("Laptop builds")
class Desktop:
    def build(self):
        print("desktop builds..")

class Alien:
    def code(self, machine: Laptop):
        # we use ( : ) just for spesific the type of the data machine its the type of class laptop
        print("Alient Building...")
        machine.build()

ds = Desktop()
pc = Laptop()
ali = Alien()
ali.code(pc)
ali.code(ds)

# another example
class Duck:
    def speak(self):
        return "Quack"

class Dog:
    def speak(self):
        return "Woof"

def make_sound(animal):
    print(animal.speak())

make_sound(Duck())  # Quack
make_sound(Dog())   # Woof


# NOTE : we must be to put the same name of the methode and the same number of parameter
class Duck:
    def speak(self):               # no extra parameter
        return "Quack"

class Dog:
    def speaks(self, volume):     # has an extra parameter
        return "Woof" * volume

def make_sound(animal):
    print(animal.speak())         # now we pass an argument

make_sound(Dog())   # WoofWoof
make_sound(Duck())  # TypeError: takes 1 positional argument but 2 were given
# NOTE 2 : 
    # IF WE WANT to add parameters in both functions (of course the same numbers ) 
    # and with the deferente values just we put parameters in the call function like [make_sound(Dog(3))] and [make_sound(Duck(1))]
    # and add the values after that when we create the functions 
# NOTE  : 
# also we can use the same name of the method but with different parameters and values in the call functiona
    # also we can use init methode to put the values and use self.(parameter in we put in the init )
    # ex : 
class Duck :
    def say(self,values):
        return "Quack\n" * values
    
class Dog:
    # we can change the name of the parameter but we put the same naumbers 
    def say(self, time ):
        return 'Woof\n' * time
    
def make_sound(animal,value):
    print(animal.say(value))         # now we pass an argument

make_sound(Dog(),5)   # WoofWoof
make_sound(Duck(),3)  # QuackQuackQuack