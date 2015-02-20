score = input("What is the score of the student? ")
score = int(score)

if score >= 0 and score <= 50:
	print("Слаб 2")
elif score >= 51 and score <= 60:
	print("Среден 3")
elif score >= 61 and score <= 70:
	print("Дoбър 4")
elif score >= 71 and score <= 80:
	print("Добър 5")
elif score >= 81 and score < 100:
	print("Отличен 6")
elif score == 100:
	print("Много Отличен 7")
else:
	print("Невалидни точки")
