import turtle
t=turtle.Turtle()

turtle.write("رمضان كريم",
font=("TimesNewRoman", 50, "normal"), move=True)

t.color("black")
t.begin_fill()

t.fillcolor("")

t.left(140)

t.forward(180)

t.circle(-90,200)

t.left(120)

t.setheading (60)

t.circle(-90,200)


t.forward(180)
t.end_fill()
a=input()
