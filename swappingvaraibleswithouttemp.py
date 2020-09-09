#swapping variables without using temporary variable

a = int(input("enter the value of a:"))

b = int(input("enter the value of b:"))

print("the values of a and b are:",a,b)

a = a+b

b = a-b

a = a-b

print("the swapped varaibles of a and b are:",a,b)