List =[1,2,3,[55,44,33],3,4,5,[40,30,30]]
#Length of List
print("Lenght of Nested list",len(List))
#Indexing of list
for i,j in enumerate(List):
    print("Indexing of Nested List",i,j)

#Given a nested list, print the element '55'.
Element=List[3][0]
print("The element is :",Element)