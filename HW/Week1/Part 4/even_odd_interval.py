a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if b > a:
	while a <= b:
		if a % 2 == 0:
			print(str(a) + " is even.")
		else:
			print(str(a) + " is odd.")
		a += 1
elif b < a:
	while b <= a:
		if b % 2 == 0:
			print(str(b) + " is even.")
		else:
			print(str(b) + " is odd.")
		b +=1
else:
	print("a is same like b")
