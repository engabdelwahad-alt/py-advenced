# it's a new class can take all attrebutes and methods from other class (subclass)
    # so we have the parent class (supperclass)
    # the child class (subcalss) 
# this is the  ; [mult lvl inheritance ]
class parent(): # grandpa
    def f1(self):
        print(" f1")

    def f2(self):
        print("f2")
# with this i can access to all attrebute and methods from parent class 
class child(parent): # parent 
    def f3(self):
        print('f3')

    def f4(self):
        print("f4")
# so  whwen we add this class so the parent will be the grandpa , child will be the parent and the child2 = child
class child2(child): #child
    def f5(self):
        print('f5')
# before the child 2 
c = child()
print('for the first child : ')
# c.f1()
# after
c = child2()
# can  access of all the classes before 
print("-"*80)
print(f"for the second child  : \n")
# c.f5()
# c.f1()
# c.f3() 
# NOTE : 
    # we can do the reversing like parent can access to the other child no only child have the access
# another type of inheritance :[ multiple inheritance ]
class A:
    def a(self):
        print("A")

    def show(self):
        print ("a number ")
class B:
    def b(self):
        print("B")

    def show(self):
        print ("b number ")
# one class can take more then one calss access
class C(B,A):
    def c(self):
        print("C")

    def show(self):
        print ("c number ")

c = C()
# one child can have more then one parents 
# c.a()
# c.b()
# c.c()

c.show()
    # so here when we call the show will be see general class first then  C(B,A) the first one here so
        # its B then A 
# NOTE : we have other option if we want to print in this exemple the A first :
    # we can use other option of style :

A.show(c)
    # A : the name of the class we want 
    # c : name of the objct we create at the first 