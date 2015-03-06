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
	return(n)

n = input("Enter n: ")
n = int(n)

small = sorted(to_digits(n))
# for debug
# print(small)
print("The smallest numbers is: " + str(numbers(small)))

big = sorted(to_digits(n), reverse=True)
# for debug
# print(big)
print("The biggest number is: " + str(numbers(big)))
