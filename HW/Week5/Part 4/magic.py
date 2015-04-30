# Used Joker 

def second_diag(matrix):
    result = 0
    row_index = 0
    col_index = len(matrix[0]) - 1

    for row in matrix:
        result += matrix[row_index][col_index]

        row_index += 1
        col_index -= 1

    return result


def main_diag(matrix):
    result = 0
    index = 0

    for row in matrix:
        result += matrix[index][index]
        index += 1

    return result


def row(matrix, index):
    return sum(matrix[index])


def col(matrix, index):
    result = 0

    for row in matrix:
        result += row[index]

    return result



def magic_square(matrix):
    sum = main_diag(matrix)

    if second_diag(matrix) != sum:
        return False

    for index in range(0, len(matrix)):
        if row(matrix, index) != sum:
            return False

    for index in range(0, len(matrix[0])):
        if col(matrix, index) != sum:
            return False

    return True

# For Test
square1 = [ [23, 28, 21], [22, 24, 26], [27, 20, 25] ]
square2 = [ [11, 24, 7, 20, 3], [4,	12,	25, 8, 16], [17, 5, 13, 21, 9], [10, 18, 1, 14, 22], [23, 6, 19, 2, 15] ]

print(square1)
print(magic_square(square1))

print(square2)
print(magic_square(square2))
