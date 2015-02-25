a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

if b > a:
	while a <= b:	
		print(a)
		a += 1
elif b < a:
	while b <= a:
		print(b)
		b +=1
else:
	print("a is same like b")
