#Quadratic function 

from math import sqrt

a = int(input("enter the value of a:"))

b = int(input("enter the value of b:"))

c = int(input("enter the value of c:"))

d = -b + math.sqrt(4ac) / 2a

d1 = -b - math.sqrt(4ac) / 2a

print("the values are:" "(" d,d1 ")")