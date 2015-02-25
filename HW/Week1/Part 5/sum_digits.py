n = input("Enter N: ")
n = int(n)

last_n = n % 10
part_n = n // 10
sum = 0

while part_n != 0:
	sum = sum + last_n
	last_n = part_n % 10
	part_n = part_n // 10

sum += last_n
print(sum)
