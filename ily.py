import turtle 

t = turtle.Turtle()
turtle.title("For You")

screen=turtle.Screen()
screen.bgcolor("white")

t.color("pink")
t.fillcolor("pink")

t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(100)

t.end_fill()

t.up()
t.setpos (-80, 150)
t.down()
t.color("white")
t.write("i love you <3", font=("Rockwell Nova", 20, "bold"))

t.ht()

turtle.mainloop()