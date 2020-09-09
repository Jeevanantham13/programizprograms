#to check the year is leap or not

year = int(input("enter the year:"))

if year % 4 == 0:
	print("it is leap year")
elif year % 400 == 0:
	print("it is leap year")
else:
	print("it is not a leap year")