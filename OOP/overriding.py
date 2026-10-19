# OVERRIDING : its a class created by the parent class and the child class create one with the same name and the same parameters 
    #  its like the same method but different job 

class Parent:
    def hello(self):
        return "hello from parent"

class Child(Parent):
    def hello(self):                  # same name as the parent's -> overriding
        return "hello from child"

    def bye(self):                    # new name, not in parent -> NOT overriding
        return "bye"
p1 = Parent()
print(p1.hello())   # hello from parent
 
c1 = Child()
print(c1.hello())   # hello from child  (parent's version is replaced)


# class person:
#     def __init__(self,name ,age):
#         self.name =name
#         self.age = age
#     def show(self):
#         print(f'name : {self.name} , age : {self.age}')
# class student(person):
#     def __init__(self,name,age,grade):
#         super().__init__(name,age)
#         self.grade = grade
#     def show(self):
#         print(f'name : {self.name} , age : {self.age} , grade : {self.grade}')