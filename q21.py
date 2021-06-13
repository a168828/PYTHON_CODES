import random;
letters="abcdefghijklimnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*";
password="".join(random.sample(letters,int(input("enter no"))));
print(password);
