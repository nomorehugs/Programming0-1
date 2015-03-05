number = input("Enter n: ")
number = int(number)

prime_numbers = [2, 3, 5, 7]
digit_list = []

while number:
    digit = number % 10
    digit_list += [digit]
    number = number // 10
    
has_prime = False
	
for digits in digit_list:
    if digits in prime_numbers:
        has_prime = True
        break

if has_prime:
    print("It has prime!!!")
else:
    print("It has NOT prime :/")
