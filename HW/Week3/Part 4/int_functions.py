def to_digits(number):
	digit_list = []
	while number:
		digit = number % 10
		digit_list += [digit]
		number = number // 10
	return digit_list
	
def numbers(digits):
	n = 0
	for digit in digits:
		n = n * 10 + digit
	return n
	
def sum_digits(n):
	digit_list = to_digits(n)
	sum = 0
	for digit in digit_list:
		sum += digit
	return sum
	
def product_digits(n):
	digit_list = to_digits(n)
	product = 1
	for digit in digit_list:
		product *= digit
	return product
	
def reverse_int(n):
	digit_list = to_digits(n)
	reverse = numbers(digit_list)
	return reverse
	
n = input("Enter a number: ")
n = int(n)

sum = sum_digits(n)
product = product_digits(n)
reverse = reverse_int(n)

print("The sum of digits in number is: " + str(sum))
print("The product of digits in number is: " + str(product))
print("The reverse number is: " + str(reverse))
	
