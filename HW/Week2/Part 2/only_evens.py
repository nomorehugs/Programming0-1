n = input("Enter count of numbers: ")
n = int(n)

sum_even = 0
count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    count += 1
    if number % 2 == 0:
        numbers = numbers + [number]
        sum_even += 1

print("Count of evens: " + str(sum_even))

for number in numbers:
	print(number)
