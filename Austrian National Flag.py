def draw_Austrian_flag():
    import turtle

    w = 900
    h = 600
    turtle.screensize(w, h, "#ed2939")
    turtle.setup(w, h)

    t = turtle.Turtle()
    t.pensize(1)
   # White in the middle
    t.pencolor("white")
    t.fillcolor("white")
    t.hideturtle()
    t.speed(10)

    t.begin_fill()
    t.penup()
    t.goto(0, -h / 3 / 2)
    t.pendown()
    t.pendown()
    t.forward(w / 2)
    t.left(90)
    t.forward(h / 3)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h / 3)
    t.left(90)
    t.forward(w / 2)
    t.end_fill()
    turtle.mainloop()

# Calling the function to draw the dutch flag
draw_Austrian_flag()