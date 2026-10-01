# set type 
#  with this we can use only one name and they change to list of carachters 
list = set('Mohammed')
#  but this is deferente not the same ecah one is an element
list2 = {'abdelawa'}
#  if we want to use set() with more element we use list inside it 
list3 = set(['ahmmed','ali'])
print(type(list))
print(list | list2)
print(list3 - list2)

# other type is Dictonory
dict_name = {'key' : 'value',
            'name':'mohammed',
            'age':'21'}

             
# #  all the dict 
# print(dict_name)
# # specific value 
# when we use this and write some thing not in the kyes we tell you error
print(dict_name['name'])
# or we can use get funct
# but this we don't do any thing 
print(dict_name.get('age'))
print(dict_name.get('ali'))
#   print anly keys 
    # we have tow 
print(dict_name.keys())
    # the second one 
for key in dict_name.keys():
    print(key)
#  for the values 
print(dict_name.values())
#  or we can also 
for value in dict_name.values():
    print(value)
# if we want to print it both so 
for key, value in dict_name.items():
    print(key,'->',value)


# we can  comverting between list and set because set has collection of keys okay 
    # and list have collection of values
#  so 
values = ['21','20','20','19','22']
keys = {'ali','moha','mehdi','taha','amine'}
# so  we have function to do converting
# so zip()  do the conbination between tow or more terables together, element by element 
result = zip(keys,values)
# we use list with zip() fo the content of the list 
print(list(result))
# if we want put is as a dictionary we must be use dict() function 
dictionary = dict(zip(keys,values))
print(dictionary)
dictionary.pop('ali')
print(dictionary)
