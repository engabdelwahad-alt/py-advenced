# Stack : FILO we dont have it in python we just the list 
# Queue : FIFO also the same thing 
    #  we created with classe 
    # we use the list but is but it is not the best option 
    #  we can also use collaction from  deque module
# so 
# we use deque without D capital because just for let here like the same of other like int,str ,list .. 
from collections import deque
# empty 
# queue = deque()     
# from a list 
queue = deque([1,2,3,5])
# fixing the size ( also they delete the lsat one and add the new one in the place)
# ex : when we put appnd they delete the the last item from the list and add the new one in this place okay
# queue = deque(maxlen=10) 
# we have extend if we want to add multiple item 
queue.extend([7,8,4,4])
print(queue)
queue.extendleft([99,77,65])
print(queue)
# the output of this is [65,77,99,1,2,3,5,7,8,4,4,]
# beaceuse when we use extendleft  it like append left so we append left the first item in the list 
# and when we append the next one the first one will be the second one  

