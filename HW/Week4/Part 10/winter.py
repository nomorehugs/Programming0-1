def winter_is_coming(seasons):  
    counter = 0
    for season in seasons:
        if season == "winter":
            counter = 0
        else:
            counter += 1
    return counter >= 5

# For Test
print(winter_is_coming(["spring", "winter", "summer","spring", "summer", "winter", "summer"]))
print(winter_is_coming(["spring", "winter", "spring", "summer", "summer", "spring", "spring"]))

