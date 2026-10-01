# exp : what is a decorators ? 
# when we use it ?
def log_deco(funct):
    def wrap(a,b):
        print ("values a : ", a , " b :", b)
        result = funct(a,b)
        print("result : ",result)
        print("*"*50)
        return result
    return wrap
def log_deco2(funct):
    def wrap(*numbers):
        # to print the values
        print ("values : ",numbers)
        result = funct(*numbers)
        print("result : ",result)
        print("*"*50)
        return result
    return wrap

def gretor_first(funct):
    def wrap(a,b): 
        if a < b:
            a,b = b,a
        # why we return funct without anything else ?
        return funct(a,b)
    return wrap
#
#  why we do this ? 
# @gretor_first
@log_deco
#  also we can do that 
# explain to me this ?
sub = gretor_first(sub)
# div = greater_first(div) 
def sub(a,b):
    print('the result of the substaraction function : ')
    return a - b

@log_deco2
# add = log_deco(add)
def add(*numbers):
    print('the resulst of the adition function : ')
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum

@gretor_first
@log_deco

def div(a,b):
    print("the result of the divistion function :")
    return a / b



sub(2,4)
# the solution of when we have more the tow argumns
add(2,4,7)
div(2,4)

# print(result1)
# print(result2)
# print(result3)
# alos  when we have three arguments and we declare only (a,b) so we use (*numbers ) as a parameters 
