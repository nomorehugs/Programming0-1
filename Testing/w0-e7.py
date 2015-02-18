book_count = 0

book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book_count = book_count + 1

book2_name = "Learn You a Haskell"
book2_price = 0
book_count = book_count + 1

book3_name = "The Healthy Programmer"
book3_price = 50
book_count = book_count + 1

book4_name = "Code Complete"
book4_price = 60
book_count = book_count + 1

book5_name = "The Pragmatic Programmer"
book5_price = 20
book_count = book_count + 1

book6_name = "Pro Git"
book6_price = 0
book_count = book_count + 1

book7_name = "Introduction to Algorithms"
book7_price = 80
book_count = book_count + 1

book8_name = "Concrete Mathematics"
book8_price = 100
book_count = book_count + 1

print("ALL BOOKS:")
print(book1_name + " for " + str(book1_price))
print(book2_name + " for " + str(book2_price))
print(book3_name + " for " + str(book3_price))
print(book4_name + " for " + str(book4_price))
print(book5_name + " for " + str(book5_price))
print(book6_name + " for " + str(book6_price))
print(book7_name + " for " + str(book7_price))
print(book8_name + " for " + str(book8_price))

print("Price of all books:")
total_sum = book1_price + book2_price + book3_price + book4_price + book5_price + book6_price + book7_price + book8_price
print(total_sum)


print("Number of all books: " + str(book_count))

discount = 25/100
normal_price = book7_price + book8_price
discount_price = normal_price - discount * normal_price	
print("Two special book for: " + str(discount_price))

print("Books for 150lv")
print("Free books:")
print(book2_name)
print(book6_name)
print("Taking books:")
print(book5_name)
print(book4_name)
print(book3_name)
print("For a total of:")
print(book5_price + book4_price + book3_price)
