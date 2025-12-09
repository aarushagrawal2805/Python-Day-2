Item =[100,300,20,500,400]
print("List Before :",Item)

#Change the second element of a list to 200 and print the updated list.
Item[1] = 200
print("List After :",Item)

#Add 600 at the end of a list and print the new list
Item.append(600)
print("List After Append :",Item)

#Insert 300 at the third position (index 2) of a list and print the result
Item.insert(2,300)
print("After insert :",Item)

#Remove 600 from the list and print the list
Item.remove(600)
print("After Remove By element :",Item)

#Remove the element at index 0 from the list print the list
Item.pop(0) #We can also use del function
print("After Remove By Index :",Item)
