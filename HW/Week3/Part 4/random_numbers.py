from random import randint

def generate_random_list(n, start, end):
	begin = 0
	rand_list = []
	
	while begin  < n:
		rand_list += [randint(start, end)]
		begin += 1
		
	return 	rand_list
	
print(generate_random_list(3, 1, 10))
print(generate_random_list(5, 3, 6))
