n = input("Enter a number: ")
n = int(n)

i = 2
is_prime = True

if n < 2:
	is_prime = False
while i < n:
	if n % i == 0:
		is_prime = False
		break
	else:
		i += 1

if is_prime:
    print("It is prime")
else:
    print("It is not prime")
