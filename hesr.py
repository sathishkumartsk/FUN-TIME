import turtle
import colorsys

t=turtl.turtle()
i=turtle.screen()
s.bgcolor('white')
t.speed(1)
n=34
h=0
for i in range(80):
    c= colorsys.hsv_to_rgb(h,1)
    h+=1/n
    t.color(c)
    t.left(5)
    for j in range (5):
        t.forward(250)
        t.left(144)
