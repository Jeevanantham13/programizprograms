#printing a random number

import random
list = []
for i in range(0,5):
	n = int(input("enter a numnber:"))
	
	list.append(n)
print(list)


randomlist=random.choice(list)
print(randomlist)