n = input("Enter count of numbers: ")
n = int(n)

count = 1
words = []

while count <= n:
    word = input("Enter new word: ")
    words += [word]
    count += 1
	
words.sort()
print(words)
