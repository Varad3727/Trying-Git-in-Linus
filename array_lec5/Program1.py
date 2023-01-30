import array 

arr1 = array.array("i",[10,20,30,40,50])
arr2 = array.array("i",[1,2,3,4,5])

arr3 = array.array("i",[])
arr4 = array.array("i",[])

for i in range(len(arr1)):
    arr3.append(arr1[i]-arr2[i])
    arr4.append(arr2[i]-arr1[i])


print(arr3)
print(arr4)


