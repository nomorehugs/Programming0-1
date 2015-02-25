a = input("Enter a: ")
a = int(a)

static_a = a
reversed = 0

while static_a != 0:
    digit = static_a % 10
    reversed = reversed * 10 + digit
    static_a = static_a // 10

if a == reversed:
	print("The number is polindrom!")
else:
	print("The number is NOT polindrom!")

