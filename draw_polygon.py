import turtle

def draw_polygon(t, sides, size):
    turn=360/sides
    for i in range(sides):
        t.forward(size)
        t.left(turn)

johnny=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")
johnny.color("pink")
johnny.pensize("3")

draw_polygon(johnny, 8, 40)

wn.exitonclick()
