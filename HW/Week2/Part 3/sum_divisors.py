n = input("Enter a number: ")
n = int(n)

count = 1
numbers = []

while count < n:
    if n % count == 0:
        numbers = numbers + [count]
    count += 1

print(numbers)

sum = 0
for number in numbers:
	sum += number

print(sum)