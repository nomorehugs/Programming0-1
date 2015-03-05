n = input("Enter a number: ")
n = int(n)

count = 1
numbers = []

while count < n:
    if n % count == 0:
        numbers = numbers + [count]
    count += 1

sum = 0
for number in numbers:
	sum += number

if n != sum:
	print("The number is NOT perfect!")
else:
	print("We have a match, it`s a perfect!!!")
