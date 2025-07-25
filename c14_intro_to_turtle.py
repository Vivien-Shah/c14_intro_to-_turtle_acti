#Polygon
##Outline:
#Write a program to set screen size, colour for turtle graphics 
# and draw a polygon using turtle
'''import turtle
turtle.Screen().bgcolor("Orange")
polygon=turtle.Turtle()
for i in range (6):
    polygon.forward(70)
    polygon.right(60)
turtle.done()'''

#Star
#Outline:
#Write a program to draw a star using a turtle?
'''import turtle
star= turtle.Turtle()
star.right(75)
star.forward(100)
for i in range (4):
    star.right (144)
    star.forward (100)
turtle.done()'''

#Spiral pattern
#Outline:
#Write a program to draw a square inside a square?
'''import turtle
spiral=turtle.Turtle()
size=0
while True :
    for i in range (4):
        spiral.forward(size+1)
        spiral.left(90)
        size=size-5
    size=size+1
turtle.done()'''
#Circle
'''import turtle

loadWindow=turtle.Screen()
turtle.speed(50)

for i in range (100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.done()'''


'''import turtle
colors=["red","purple","blue",
    "green","orange","yellow"]
my_pen=turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colors[x%6])
    my_pen.width(x/100+1)
    my_pen.forward(x)
    my_pen.left(59)'''









