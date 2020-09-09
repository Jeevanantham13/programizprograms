# to print the prime numbers

num = int(input("Enter a number: "))
for i in range (2,num):
    if num%i==0:
        print("it is not a primenumber")
        break
else:
        
    print("it is a primenumber")
        