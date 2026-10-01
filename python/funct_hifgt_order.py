#  so w can call a function  in another function as an argumnet so
#  we create tow fun 
def sqaure(number):
    return number * number
#  the in the paremeters we put tow so 
    #  1 for the number (value)
    # 2  for the function we want to use 
def operate(number,opperation):
    # this how we call inside the function 
    #  we declarate in as an argument whwn we call this function 
    return opperation(number)

result = operate(5,sqaure)
print(result)

# NOTE 
#  we have tow thing 
#  when we put 
    #  varible = function 
        # that storage the function 
    #  varibel =  function() 
        # that mean storage the return of the function (result)    