#  lambda : we use it when we want to do a simple thing without create a function (quick, throwaway function)
    #  like if we want to return ( number * number )
# expmle : 
# def square(num):
#     return num * num 
# so we can't do all this just for one line return so we use lambda in one line
# so 
#  lambda paramaters : expression and we storage in a varible for use it 
sq = lambda num: num * num
# note / we put the same name in parameter and expresion why :
# because in expresion don't know the varible so must be declare it in paramater so if we have deferete var so we declare it both 
# lambda num,x,y : (num * x) + y 
sq(3)
print(sq)





