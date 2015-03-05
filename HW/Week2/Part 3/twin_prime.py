n = input("Enter a number: ")
n = int(n)

i = 2
is_prime = True

n1 = n - 2
n2 = n + 2

if n < 2:
	is_prime = False
while i < n:
	if n % i == 0:
		is_prime = False
		break
	else:
		i += 1
		
i = 2
is_n1_prime = True		
		
if n1 < 2:
	is_n1_prime = False
while i < n1:
	if n1 % i == 0:
		is_n1_prime = False
		break
	else:
		i += 1
		
i = 2
is_n2_prime = True		
		
if n2 < 2:
	is_n2_prime = False
while i < n1:
	if n2 % i == 0:
		is_n2_prime = False
		break
	else:
		i += 1
		
if is_prime and (not is_n1_prime) and (not is_n2_prime):
    print(str(n) + " is prime")
    print("But " + str(n1) + " and " + str(n2) + " are not.")
elif is_prime:
    if is_n1_prime:
        print("Twin brother with: " + str(n))
        print(n1, n)
    if is_n2_prime:
        print("Twin brother with: " + str(n))
        print(n, n2)
else:
    print(str(n) + " is not prime.")
