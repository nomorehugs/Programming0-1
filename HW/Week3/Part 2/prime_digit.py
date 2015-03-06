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
	
def to_digits(number):
	digit_list = []
	while number:
		digit = number % 10
		digit_list += [digit]
		number = number // 10
	return digit_list
	
n = input("Enter n: ")
n = int(n)

prime_digit = False

for digits in to_digits(n):
    if is_prime(digits):
        prime_digit = True
        break

if prime_digit:
    print("It has prime!!!")
else:
    print("It has NOT prime :/")
