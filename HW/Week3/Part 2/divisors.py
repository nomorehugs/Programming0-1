def divisors(n):
	count = 1
	numbers = []
	while count < n:
		if n % count == 0:
			numbers = numbers + [count]
		count += 1
	return numbers
	
n = input("Enter n: ")
n = int(n)

print(divisors(n))