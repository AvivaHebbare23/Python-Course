import turtle

turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup(600, 550)

pen = turtle.Turtle()

sides = 4
side_Length = 70
angle = 360 / sides

for i in range(sides):
    pen.forward(side_Length)
    pen.right(angle)

turtle.done 