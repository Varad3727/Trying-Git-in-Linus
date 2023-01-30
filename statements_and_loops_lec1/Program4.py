list1 = [1]
for i in list1:
    a = int(input("Enter the marks of first guy: "))
    b = int(input("Enter the marks of second guy: "))
    c = int(input("Enter the marks of third guy: "))
    if(a>b):
        if(a>c):
            print("Marks of first guy is greater than second and third guy")
        else:
            print("Marks of first guy is greater than second guy but less than third guy")
    else:
        if(a>c):
            print("Marks of first guy is less than second guy but less than third guy")
        else:
            print("Marks of first guy is less than second and third guy")
    choice = input("Enter the 'yes' if you want to continue and 'no' if you want to exit: ")
    if(choice!='no'):
        #incrementer+=1
        #print(incrementer)
        list1.append(i)

