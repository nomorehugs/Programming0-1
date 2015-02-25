a = input("Enter a: ")
a = int(a)

reversed = 0

while a != 0:
    digit = a % 10
    reversed = reversed * 10 + digit
    a = a // 10

print("The reversed number is: " + str(reversed))
