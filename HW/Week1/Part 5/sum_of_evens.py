n = input("Enter N: ")
n = int(n)
count = 1
sum = 0

while count <= n:
	if count % 2 == 0:
		sum = sum + count
		count += 1
	else:
		count += 1
	
print(sum)
