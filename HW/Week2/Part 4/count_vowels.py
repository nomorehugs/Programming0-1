words = input("Enter something: ")

vowels = "aeiouyAEIOUY"
count = 0

for ch in words:
    if ch in vowels:
        count += 1

print("The number of vowels is: " + str(count))
