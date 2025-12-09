#Remove Duplicates from list

List1=[1,2,3,1,2,3,4,5,6,4,3]

#Convert it into set,It help to remove duplicate value
List2=set(List1)
print(List2)

#Now After remove duplicate value again convert into List
List4=list(List2)
print("Original List :",List1)
print("No duplicate Value List :",List4)