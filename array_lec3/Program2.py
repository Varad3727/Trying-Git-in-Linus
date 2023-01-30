import array

arr = array.array("i",[10,20,30,40,50,60,70,80,90])

print(arr[2:4:])
print(arr[3::])
print(arr[:7:])
print(arr[:8:3])
print(arr[::2])
print(arr[-3::])
print(arr[:-6:])
print(arr[-3:-8:])  # the end value should be greater than the start value by defalt (blank o/p)
print(arr[-3:-8:-2])  # if the step value is -ve the the start value should be greater then end
print(arr[::-4])
print(arr[2:8:-2])
print(arr[:8:-3])
print(arr[9:5:3])
