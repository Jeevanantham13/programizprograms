# to print the prime numbers

num = int(input("Enter a number: "))
for i in range (2,num):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
       
        
    
        
       
        