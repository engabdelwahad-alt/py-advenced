# filtering : its a function return a list that give the result of an condition
ls = [1,3,4,5,6]
# fact = lambda number : number % 2 == 0
# evens = list(filter(fact,ls))
    # the list for print it as a list 
    # filter is a function 
        # fact is the condition 
        # ls : is the name of the list 
# also we can use this 
evens = list(filter(lambda number : number % 2 == 0 , ls))
# filter take all elements one by one and check the function and return (T/F)
print("the pair number in the list : ",evens)

#  MAP() : is take the items from the list and do the change elements by elements with condition put in the list return (T/F)
# ex:
doubl = list(map(lambda number : number * number , ls))
print("double the list : ",doubl)
# we can use the list of the feltring 
def f(n):
    return n * 2
# this double the filter list (pair number) and double it 
double_even = list(map(f,evens))
print("double evens : ",double_even)
print(sum(ls))