import array

arr = array.array('I',[10,30,20,30,40,30,20])
arr2 = array.array('f',[10.8,40.5,30.7,20.8])

print(arr.buffer_info())
print(arr2.buffer_info())



