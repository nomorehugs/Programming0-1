n = input("Enter N: ")
n = int(n)

last_n = n % 10
part_n = n // 10

while part_n != 0:
	print(last_n)
	last_n = part_n % 10
	part_n = part_n // 10

print(last_n)
