from turtle import *

colormode(255)

def  fleur():
    for i in range(255):
        color((i,(255-i),255))
        begin_fill()
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        end_fill()

speed(0)
fleur()

mainloop()