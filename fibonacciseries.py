#fibonacci series using for and while loop

loop =int(input("if you want to execute fibonacci series in for loop enter 1:"))

if loop == 1:

	terms = int(input("enter how many terms in the series wants to print:"))
	
	for i in range(2,terms):
	
		fibonacci = (i-1) + (i-2)
		
		print(fibonacci)
		

    
    