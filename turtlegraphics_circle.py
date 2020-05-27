'''This file imports python graphic module "turtle"
   This program draws a circle
   Author: Uday   Time stamp: 5/27/2020'''
import turtle
wn=turtle.Screen()
jess=turtle.Turtle()
jess.pensize(5)
jess.shape('turtle')
jess.speed(0)
jess.penup()
for i in range(360):
    jess.forward(350)
    jess.stamp()
    jess.backward(350)
    jess.left(1)
turtle.exitonclick()
