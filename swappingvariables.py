#swapping the varaibles

a = int(input("enter the value of a:"))

b = int(input("enter the value of b:"))

temp = int(input ("enter the temporary variable:"))

print("the values of a and b are:",a,b)

temp = a

a = b

b = temp

print("the swapped varaibles of a and b are:",a,b)
