#Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = []
#zip()it joins two lists
#i+j it add to same pair
for i,j in zip(list1,list2):
    list3.append(i+j)

print(list3)

#DRY RUN

'''for 1,1 in zip(list1,list2):
    lsit3append(m+y)
    
    list3['My']'''