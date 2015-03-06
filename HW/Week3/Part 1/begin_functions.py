def square(x):
	return x * x
	
def fact(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def count_elements(items):
	result = 0
	for item in items:
		result += 1
	return result
	
def member(x, xs):
	result = False
	start = 0
	end = len(xs) - 1
	while start <= end:
		if xs[start] == x:
			result = True
		start += 1
	return result

def grades_that_pass(students, grades, limit):
	good_students = []
	index = 0
	for grade in grades:
		if grade >= limit:
			good_students += [students[index]]
		index += 1	
	return	good_students	
	
