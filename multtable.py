n = int(input("enter a number:"))

times = int(input("enter how many times n should be multiplied:"))

for i in range(0,times+1):
	ans = n * i
	
	print(n,"*",i,"=",ans)