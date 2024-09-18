import turtle
turtle.bgcolor("black")
t=turtle.Turtle()

t.speed(0) 
colors=["blue","dark blue"]

for number in range(400):
    t.forward(number)
    t.right(89)
    t.pencolor(colors[number%2])
turtle.done()   
