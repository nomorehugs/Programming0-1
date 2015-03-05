number = input("Enter n: ")
number = int(number)

digits = []

while number:
    digit = number % 10
    digits = [digit] + digits
    number = number // 10
    
print(digits)

n = 0
for digit in digits:
    n = n * 10 + digit
	
print(n)
