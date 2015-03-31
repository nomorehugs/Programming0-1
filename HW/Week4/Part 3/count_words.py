def count_words(words):
    dict = {}
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

# For Test
#print(count_words(["words", "are", "meaningful", "words", "Words", "are"]))
