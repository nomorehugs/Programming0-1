def count_zero_pairs(numbers):
    count = 0
    n = len(numbers)
    
    for x_index in range(0, n):
        for y_index in range(x_index, n):
            x = numbers[x_index]
            y = numbers[y_index]

            if x + y == 0:
                count += 1

    return count
	
# For Test
print(count_zero_pairs([0, 2, -2, 5, 10]))
