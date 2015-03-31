def count_vowels_consonants(word):
	dict = {"vowels": 0, "consonants": 0}
	vowels = "aeiouyAEIOUY"
	consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	for ch in word:
		if ch in vowels:
			dict["vowels"] += 1 
		if ch in consonants:
			dict["consonants"] += 1
	return dict
	
# For Test
#print(count_vowels_consonants("aaaAcccD"))
#print(count_vowels_consonants("aaaA"))
#print(count_vowels_consonants("ccD"))
		
