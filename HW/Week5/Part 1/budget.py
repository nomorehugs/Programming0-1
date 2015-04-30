def on_budget(books, budget):
	in_budget = {"book_on_budget": 0, "loan": 0}
	count = 0
	total = sum(books)
	books = sorted(books)
	
	for book in books:
		if budget - book < 0:
			break
			
		budget -= book
		total -= book
		count += 1

	in_budget["book_on_budget"] = count
	in_budget["loan"] = max(0, total - budget)
	
	return in_budget
	
# For Test
print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 100], 20))
print(on_budget([40, 30, 40], 30))
