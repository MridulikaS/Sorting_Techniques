aList =[ 12 ,1,6,13,-56,22,3,52,2,-1,0]
print("Original list is:" , aList)
n=len(aList)

#traverse through all list elements
for i in range (n):
    #Last i elements are already in place

    for j in range (0,n-i-1):
        print(aList[j],aList[j+1])

        if aList[j]>aList[j+1]:
            aList[j],aList[j+1]=aList[j+1],aList[j]

    print("List after bubble sort:" , aList)
