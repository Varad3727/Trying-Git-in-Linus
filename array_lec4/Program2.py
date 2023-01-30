import array

arr = array.array("i",[])

num = int(input("Enter the number of elements you want in an array: "))

sum = 0

for i in range(num):
    a = int(input("Enter the element: "))
    if(a%2==0):
        sum+=a
    arr.append(a)

print(arr)
print(sum)

temp = sum
rev = 0
while(temp>0):
    rev = rev*10 + temp%10
    temp//=10 # we used double division symbol because single division symbol will give result as decimal number

print(rev)



