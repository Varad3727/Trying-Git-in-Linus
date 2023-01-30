num1 = int(input("Enter the number: ")) 
num2 = int(input("Enter the number: "))
if(num1>num2):
    num1 = num1+num2
    num2 = num1-num2
    num1 = num1-num2
count = 0
for x in range(num1,num2+1):
    if(x%4==0):
        count+=1
print(count)



