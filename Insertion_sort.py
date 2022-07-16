aList =[ 12 ,1,6,13,-56,22,3,52,2,-1,0]
print("Original list is:" , aList)

for i in range (1,len(aList)):
    print(i)
    key = aList[i]
    print(key)
    j=i-1
    print(j)
    while j>=0 and key<aList[j]:
        aList[j+1]=aList[j]
        j=j-1
        print('key,j:',key,j)
        print(aList)
    else:
        aList[j+1] = key
        print(aList)

    print("List after sorting:" , aList)