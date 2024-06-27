import math


# 1
def degree_to_radian(degree):
    return degree * (math.pi / 180)


input_degree = 15
output_radian = degree_to_radian(input_degree)
print(f"Output radian: {output_radian:.6f}")


# 2
def area_trapezoid(base1, base2, height):
    return (base1 + base2) * height / 2


height = 5
base1 = 5
base2 = 6
area = area_trapezoid(base1, base2, height)
print(f"Expected Output: {area}")
# 3
def area_regular_polygon(n, s):
    return (s ** 2 * n) / (4 * math.tan(math.pi / n))


num_sides = 4
length_side = 25
area = area_regular_polygon(num_sides, length_side)
print(f"The area of the polygon is: {area}")
#4
def area_parallelogram(base, height):
    return base * height

base = 5
height = 6
area = area_parallelogram(base, height)
print(f"Expected Output: {area:.1f}")
