a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

last_a = a % 10
last_b = b % 10

if last_a > last_b:
	print("Bigger last number is from: " + str(a))
elif last_a < last_b:
	print("Bigger last number is from: " + str(b))
elif a > b:
	print("Last number are same and bigger whole number is: " + str(a))
elif a < b:
	print("Last number are same and bigger whole number is: " + str(b))
else:
	print("The numbers are same: " + str(a))
	