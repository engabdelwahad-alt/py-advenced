#  we have tow type of linkedlist 
    #  singly and doubly 
    # the singly have just tow (data + address for the next node) 
    #  but the doubly have three (data + address for the next node + address for the perv node )
        #  so we can go and comeback
# and in python when we want to use it we use it by calsses
# 1- singly
class Node:
    #  we don't put next as a paremater because we don't use it 
    # and we don't do any change of the addresses only the data
    def __init__(self,data):
        self.data = data
        # None mean null (nothing)
        self.next = None
#  we this class we use current alot because in this class we self is an objecet has head of the class (SinglyLinkedlist) and do not has data or next 
    # (data and next is for Node )  
    # so we use current because is it an object have of the class (Node) has ( data and next) but dont have head
class SinglyLinkedlist:
    def __init__(self):
        # the first node 
        self.head = None    
    def append(self,data):
        new_node = Node (data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def print_list(self):
        current = self.head
        # we use current in the while because for ceack if the current it's a reale node or not(not None) 
        while current:
            #  we use end beause in python we adds new line automateclly like (\n)
            #  (end ) its like to say to the print funct to end with sting not with new line okay
            print(current.data, end = " -> ")
            current = current.next
        print("None")
    def search(self,varible):
        current = self.head
        while current:
            if current.data == varible:
                print("exit")
                print(f"the address of this is : {current.next} and the data is {current.data}")
            current = current.next
            return True
    def remove(self,target):
        current = self.head 
        previous = None
        while current: 
            if current.data == target:
                #  this for delete the head 
                if previous is None:
                    self.head = current.next
                else:
                    # this is put the add of the node before mean (address of the node before the remove node )
                    # for conected after that with the node after the remove node 
                    # in  this the next of the node we dellted we put it in the next  of the previous 
                    previous.next = current.next
                    #  after that = previous has in her .next the .next of the remove node 

                return True
            # put the prev and current point to the same node 
            # because after that the current point to the remove node so we need to put it to point to the node after the remove 
            previous = current
            # then we put it to point to the .next node (tow node after the remove node )for cheaking the others node and conyinue all the node okay 
            current = current.next
        return False
    def modify(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value       # just overwrite the data
                return True
            current = current.next
        return False                            # old_value not found




sl = SinglyLinkedlist()
sl.append(1)
sl.append(2)
sl.append(3)
sl.append(4)
sl.append(5)
sl.append(6)
sl.append(0)
sl.print_list()

sl.remove(6)

sl.search(5)

sl.modify(0,99)

sl.print_list()
















