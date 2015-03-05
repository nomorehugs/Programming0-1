main_word = input("Enter word: ")

n = input("Enter count of numbers: ")
n = int(n)

count = 1
count_word = 0

while count <= n:
    word = input("Enter new word: ")
    if main_word == word:
        count_word += 1

    count += 1

print(main_word + " is found " + str(count_word) + " time(s)!")
