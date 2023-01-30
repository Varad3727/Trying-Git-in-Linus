list1 = [10, 20.63, 'Varad']
list2 = [10,20.63,'Varad']

print(list1)
print("list1->id = " +'%s'%id(list1))
print("list2->id = "+'%s'%id(list2))

print("list1[0]->id (before changing) = "+'%s'%id(list1[0]))
print("list2[0]->id = "+'%s' % id(list2[0]))

list1[0] = 50

print("list1[0]->id (after changing) = " + '%s' % id(list1[0]))
print("list1->id = "+'%s'%id(list1))
print("list2->id = "+'%s'%id(list2))






