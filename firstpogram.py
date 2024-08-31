#create list and add,remove,modify the list
my_list = [1,2,3,4,5]
print(my_list)
my_list.append(6)
print("add list",my_list)
my_list.remove(6)
print("remove list",my_list)
my_list[2] =100
print("modify list",my_list)

#create dictionary and add,remove,modify the dictionary
my_dictionary={'name': 'jaga mohan','age': 20}
print(my_dictionary)
my_dictionary['city']='Bhubaneswar'
print("after add",my_dictionary)
my_dictionary.pop('city')
print("after remove",my_dictionary)
my_dictionary['age']=24
print("after modify",my_dictionary)

#create dictionary and add,remove,modify the dictionary

my_set ={10,20,30,40}
print (my_set)
my_set.add(50)
print("after add",my_set)
my_set.remove(40)
print("after remove",my_set)
my_set.update([60,70])
print("after update",my_set)
