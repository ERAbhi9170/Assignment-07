print("Input lengths of the triangle sides: ")
x,y,z=int(input("x: ")),int(input("y: ")),int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("not triangle")