#első feladat 9.dk
from os import sep


a=int(input("kérek egy számot: "))
b=int(input("kérek még egy számot: "))
c=input("kérek egy müveletett: ")
if  c=="+":
    print(a+b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="-":
    print(a-b)