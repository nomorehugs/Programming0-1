n = input("Enter a 3-digit number: ")
n = int(n)

if n // 1000 != 0:
    print("The number is not 3-digit!")
else:   
    z = n % 10
    n = n // 10

    y = n % 10
    n = n // 10

    x = n % 10

    largest = x

    if y >= largest and y >= z:
        largest = y

    if z >= largest and z >= y:
        largest = z
            
    smallest = x

    if y <= smallest and y <= z:
        smallest = y

    if z <= smallest and z <= y:
        smallest = z

    middle = z

    if (largest == z and smallest == y) or (smallest == z and largest == y):
        middle = x
    elif (largest == z and smallest == x) or (smallest == z and largest == x):
        middle = y

    max_number = largest * 100 + middle * 10 + smallest
    min_number = smallest * 100 + middle * 10 + largest

    print("Max number with those digits is: " + str(max_number))
    print("Min number with those digits is: " + str(min_number))
