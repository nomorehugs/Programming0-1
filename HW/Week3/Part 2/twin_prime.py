def is_prime(n):
	i = 2
	prime = True

	if n < 2:
		prime = False
	while i < n:
		if n % i == 0:
			prime = False
			break
		else:
			i += 1
	return 	prime

n = input("Enter a number: ")
n = int(n)

n1 = n - 2
n2 = n + 2
		
if is_prime(n) and (not is_prime(n1)) and (not is_prime(n2)):
    print(str(n) + " is prime")
    print("But " + str(n1) + " and " + str(n2) + " are not.")
elif is_prime(n):
    if is_prime(n1):
        print("Twin brother with: " + str(n))
        print(n1, n)
    if is_prime(n2):
        print("Twin brother with: " + str(n))
        print(n, n2)
else:
    print(str(n) + " is not prime.")
