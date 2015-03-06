def divisors(n):
	count = 1
	numbers = []
	while count < n:
		if n % count == 0:
			numbers = numbers + [count]
		count += 1
	return numbers
	
def sum_ints(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum
	
def is_perfect(x):
	return x == sum_ints(divisors(x))
	
n = input("Enter n: ")
n = int(n)

#divisor = divisors(n)
#print(divisor)
#sum = sum_ints(divisor)
#print(sum)

perfect = is_perfect(n)
print(perfect)
