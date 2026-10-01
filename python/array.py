#  array 
from array import *
# the ini
# the 'i' for spesific what we want to storge in the list with the range 
    # the uppercase (H,B,I,..) this have deferece range but only positive with zero 
    # the lowercas (b,h,i,d..) also deference range but we can allowed the positive and the negative

arr1 = array('i',[1,2,4,-5,6])
# when we do that arr1 and arr2 take the same address
# if we do any change the chage will be in the both array
arr2 = arr1

arr2.append(100)
#  we append arr2 but also arr1 will appended automatecly
print(type(arr1))
print(arr1)
print(arr2)
    # this is print all this  array('i',[1,2,4,-5,6])
# we want to print only the values 
print(arr1.tolist())
    # if we want to print it one by one we use  loop and print(i)
print(arr1.buffer_info())
print(arr2.buffer_info())

    # this for show the address and the size 
arr1.reverse()
for i in arr1:
    print(i)

#  if we want to create an empty array and copy the element in the new array so we do that 
arr3 = array('i',arr1.tolist())
    #   tolist is a function returned the list we can use here or in print iff we want 
# if we dont know the type of the element in the list so we can use this function
arr4 = array(arr1.typecode,arr1.tolist())
print(arr3)
print(arr4)
