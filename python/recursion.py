#  how we calcl the fuctorial with to method 
def f(number):
    result = 1
    for i in range(number):
        result = result * (number - i)
    return result
fact = f(int(input("enter the number  : ")))
print(fact)
# also we can calc with 
#  recursion is a functoin call him selef
def facturial(number):
    if number <= 1:
        return 1
    
    return number * facturial(number - 1)
result = facturial(5)
print(result)