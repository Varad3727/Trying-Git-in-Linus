import array

arr1 = array.array("i",[10,20,30])

print(arr1)

arr2 = arr1

print(arr2)

print(id(arr1))
print(id(arr2))


