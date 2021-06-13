def checkList(list1,item):
    if item in list1:
        return True;
    else:
        return False;
b=[1,2,3,4,5,6,7,8,9,10,11,12,13];
num=int(input("enter a no"));
check=checkList(b,num);
print(f"{check} the {num} is in the list");
