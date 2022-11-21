from turtle import *
from random import randint

speed(0)
bgcolor("black")
for x in range(1,600):
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(50+x)
    right(90.911)
    x+=1
mainloop()