def is_triangle(x, y, z):
    return x + y > z > 0 and y + z > x > 0 and x + z > y
		
def area(x, y, z):
	p = (x + y + z) / 2
	return (p*(p-x)*(p-y)*(p-z)) ** 0.5

def is_pythagorean(x, y, z):
	return (x ** 2 + y ** 2) == z ** 2

def max_area(triangles):
    max = triangles[0]
    x = max[0]
    y = max[1]
    z = max[2]
    max_area = area(x, y, z)

    for triangle in triangles:
        x = triangle[0]
        y = triangle[1]
        z = triangle[2]
        triangle_area = area(x, y, z)

        if triangle_area > max_area:
            max = triangle
            max_area = triangle_area

    return max
	
print(is_triangle(2,3,5))
print(is_triangle(4,3,5))

print(area(2,3,5))
print(area(3,4,5))
print(area(7,8,9))

print(is_pythagorean(4,3,5))
print(is_pythagorean(5,6,7))

triangles = [ [3, 4, 5], [7, 8, 9] ]

print(max_area(triangles))
