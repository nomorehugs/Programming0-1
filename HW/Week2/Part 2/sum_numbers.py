n = input("Enter count of numbers: ")
n = int(n)

count = 1
sum = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    sum += number
	
    count += 1

print("The sum is: " + str(sum))
