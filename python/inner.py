# inner (nested funtion ) : it's a function definde inside another function :
    # we can't call the inner function out side the outer function because is not defind

def out(inner):
    print("in outer function ")
    def inner():
        print("in inner function ")
    # we call it inside the big function
    # inner()
    return inner
# when we put varible = fun() that mean the varible has what the functoin return 
    # so in this point the out function return inner function
x = out()
# that mean call whatever x point to so they call inner function
x()