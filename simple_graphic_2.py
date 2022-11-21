from turtle import *
from random import randint


colormode(255)
bgcolor("black")
pensize(1)
speed(0)
for i in range(1,101):
    color(randint(100,156),randint(100,156),randint(100,156))
    circle(i*3+5,120)
    left(90)
    i+=1
mainloop()
