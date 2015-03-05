n = input("Enter count of numbers: ")
n = int(n)

count = 1
numbers = []
sum = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    sum += number
    numbers = numbers + [number]
		
    count += 1

avg = sum/len(numbers)
print("Avg. is:  " + str(avg))
