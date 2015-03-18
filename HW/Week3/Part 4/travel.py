def travel_cost(travels):

	sum = 0 
	
	for travel in travels:
		if travel >= 23:
			sum += 23
		else:
			sum += travel
		
		if sum >= 50:
			sum = 50
			
	return sum
	
print(travel_cost([32, 3, 29]))
print(travel_cost([32, 10, 23]))
print(travel_cost([1, 4, 10, 1, 2, 20, 10, 1, 9]))
print(travel_cost([1, 1, 1, 1]))
