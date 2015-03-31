def get_people_count(activity):
    counted = []
    for person in activity:
        if person not in counted:
            counted += [person]
    return len(counted)

# For Test
print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))

