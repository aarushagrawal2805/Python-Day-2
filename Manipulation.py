Item =[100,300,20,500,400]
print("List Before :",Item)

#Change the second element of a list to 200 and print the updated list.
Item[1] = 200
print("After changing second element :",Item)

#Add 600 at the end of a list and print the new list
Item.append(600)
print("List after appending 600 :",Item)

#Insert 300 at the third position (index 2) of a list and print the result
Item.insert(2,300)
print("List after inserting 300 at index 2:",Item)

#Remove 600 from the list and print the list
Item.remove(600)
print("List after removing 600 (by value) :",Item)

#Remove the element at index 0 from the list print the list
Item.pop(0) #We can also use del function
print("List after removing element at index 0 :",Item)
