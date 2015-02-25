# Трябваше да ползваш жокер, че логиката която вкарвах в предните задачи в тази стана сложна за дебъгване и грешна

a = input("Enter a: ")
a = int(a)

b = input("Enter b: ")
b = int(b)

lower_bound = 0
upper_bound = 0

if a < b:
    lower_bound = a
    upper_bound = b
elif a > b:
    lower_bound = b
    upper_bound = a
else:
	print("The numbers are same!")
	
start = lower_bound

while start <= upper_bound:

    n = start
    total_sum  = 0
    
    while n != 0:
        digit = n % 10
        total_sum = total_sum + digit
        n = n // 10

    print("total_sum of digits of " + str(start) + " = " + str(total_sum))
    start += 1

