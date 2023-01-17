#6
from turtle import *
left(90)
k=20
for i in range(3):
    right(45)
    forward(15*(2**0.5)*k)
    right(180-45)
    forward(15*k)
    right(90)
    forward(15*k)
    right(90)
pu()
for x in range(17):
    for y in range(17):
        goto(x*k,y*k)
        dot(5)
