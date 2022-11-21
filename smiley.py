import turtle
 
turtle.speed(8)
#define pen size
turtle.pensize (5)
 
#define pen color
turtle.pencolor ("black")
 
#for outer bigger circle
turtle.fillcolor("yellow")
turtle.penup ()
turtle.goto (0, -200)
turtle.pendown ()
turtle.begin_fill ()
turtle.circle (200)
turtle.end_fill ()
 

#for eyes
turtle.fillcolor ("black")
turtle.penup ()
turtle.goto (-90,40)
turtle.pendown ()
turtle.begin_fill ()
turtle.circle (50)
turtle.end_fill ()
turtle.penup ()
turtle.goto (90,40)
turtle.pendown ()
turtle.begin_fill ()
turtle.circle (50)
turtle.end_fill ()
 

 
# for smile
turtle.penup ()
turtle.goto (-100, -70)
turtle.pendown ()
turtle.begin_fill ()
turtle.right (90)
turtle.circle (100,180)
turtle.left(90)
turtle.forward(200)
turtle.end_fill ()
turtle.mainloop ()


face()

mainloop()
    