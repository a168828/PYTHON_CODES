def concat(list1, list2):
    return list1+list2

list1=[]
list2=[]
list1 = [int(items) for items in input("Enter the list: ").split()]
list2=[int(items) for items in input("Enter the second list: ").split()]
list3=[]
list3 = concat(list1, list2)
print(list3)
