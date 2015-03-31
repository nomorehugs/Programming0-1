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
	
def prime_pair(numbers):
    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                return True

    return False
	
# For Test
print(prime_pair([1, 2, 3, 4, 5]))