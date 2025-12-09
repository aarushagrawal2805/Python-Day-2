#List Comprehension for Numbers using isinstance(object,(type))
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

#Sort only string
list1=[item for item in my_list if isinstance(item,(str))]

print(list1)
#Sort only no.
list2=[item for item in my_list if isinstance(item,(int,float))]

print(list2)
