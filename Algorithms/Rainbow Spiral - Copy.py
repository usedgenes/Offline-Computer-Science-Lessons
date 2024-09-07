from turtle import *
speed(0)

J1,J2 = (250,210,70),(253,190,25)
NR, BL = (0,0,0), (255,255,255)

def cercle(x,y,r,c):
  e = 2 * r
  penup()
  setheading(0)
  goto(x,y - r)
  color(c)
  pensize(e)
  pendown()
  circle(r)

cercle(0,0,40,J1)
# Yeux
cercle(-28,22,15,J2)
cercle(28,22,15,J2)
cercle(-28,22,10,BL)
cercle(28,22,10,BL)
cercle(-28,22,5,NR)
cercle(28,22,5,NR)
# Bouche
for i in range(-35,36,5):
  cercle(i,-35,10,NR)
for i in range(-35,36,5):
  cercle(i,-35,5,BL)   
# Dents
color(NR)
pensize(1)
for i in range(-3,4):
  penup()
  goto(-10*i,-20)
  pendown()
  goto(-10*i,-45)
penup()
goto(-45,-35)
pendown()
goto(45,-35)
hideturtle()