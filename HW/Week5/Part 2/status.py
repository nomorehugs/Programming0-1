def status_count(students):
	at_end = {
                "finalized": [],
                "not_finalized": []
                }
	
	for student in students:
		if student["status"] is "not_finalized":
			at_end["not_finalized"] += [student["name"]]
		else:
			at_end["finalized"] += [student["name"]]
			
	return at_end
	
# For test
students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))
