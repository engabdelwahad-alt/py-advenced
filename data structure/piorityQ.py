# priorety Queue its FIFO but with (highest or smolest preiorety first )
#  so in python we use heapq module
import heapq
pq = []
pq2 =[]
# we add the items in the list like this 
#  this automaticly put it from the lowest to the highest
# (pq = mean the name of the list , second one = mean the items )
heapq.heappush(pq,5)
heapq.heappush(pq,4)
heapq.heappush(pq,33)
print(pq)
# and  we have the string we use deferente think we compare the alphabet 
# so a before b sof if we have upper and lower cases so in this point
        # the uppercase is before the lowercase
heapq.heappush(pq2,"hello")
heapq.heappush(pq2,"Good")
heapq.heappush(pq2,"upper")
print(pq2)
#  also when we have the tuple
#  in this point we compare the first elementes if there is same go to the second one
#  

tasks = []
heapq.heappush(tasks, (1, "wash dishes"))
heapq.heappush(tasks, (1, "put out fire"))
heapq.heappush(tasks, (3, "watch TV"))
print(tasks)
#  we have a function if we alreay have an list no empty so we use heapify function
words = ["banana", "apple", "cherry"]
heapq.heapify(words)
print(words)
# all function we have in this module we need it :
# heap = mean the name of the list 
        # heapq.heappush(heap, item)
        # heapq.heappop(heap) remove and deleted the lowest items
        # heapq.heapreplace(heap, item) deleted the lowest and add the an items 
        # heapq.heapify(list) 
        # heapq.nlargest(n, iterable) return the bigest one  
            # n = mean for ex top 3 or 4 loke that okay 
            # iterable = mean the name of list from where list or tuple or any place you want to do this 
        # heapq.nsmallest(n, iterable) the smallest one 
        # heap[0] the samlest one beause its the first one
        # heapq.merge(*iterables)
        # heapq.heappushpop(heap, item)
            # this is return the smallest items in the  list 
            #  so we pop it the head item and compare it with the smallest  in the list so 
                # if : the new item smalleset  then the head so we unchange the list stay and return the new item 
                #  else : they pop it the head and push it the new item and put in the right place and return smallest one in the old list (head) 
