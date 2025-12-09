List1=["Aryan",20,20.000]
List2=["Amit",20,15.000]
print("List 1: ",List1)
print("List 2: ",List2)

#Combine given two lists into a single list and print it

#Combine using Extend Keyword
List1.extend(List2)

print("Combine of Both List : ",List1)

#Combine Using + Operator
List3 = ["New Joining"]
print("Combine using + Operator :",List1 + List3)