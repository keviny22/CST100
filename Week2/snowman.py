#Snowman, by Kevin Young

#In this assignment you will use the `turtle` python module to draw a snowman. You may NOT use the Turtle.circle function to draw circles.
#
#Snowman:
#
#·      The snowman should be on a blue background, and should be drawn filled with white.
#·      The outline of the snowman should be in black.
#·      The snowman’s body should be made of 3 filled circles.
#·      The outline of each circle should be 3 pixels wide.
#·      The bottom circle should have a radius of 100 pixels.
#·      The middle circle should have a radius of 70 pixels.
#·      The top circle should have a radius of 40 pixels.
#·      Each circle should be centered above the one below it (except the bottom circle, which can be located anywhere).
#·      There should be no gap between the circles.
#·      Give the snowman a mouth, eyes, and a nose (a hat is optional).
#·      Make sure to include two stick-arms and at least two fingers on each hand.


import turtle
import math
screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Frosty the snowman!")

frosty = turtle.Turtle()
frosty.speed(0)
frosty.color("black")
frosty.fillcolor("white")
frosty.pensize(3)
frosty.hideturtle()

# A function for drawing a face (eyes, mounth, nose)
# by supplying the coordinate for the center of the eyes
def Face(x,y):
    frosty.up()
    frosty.goto(x + 10,y)
    frosty.dot()
    frosty.goto(x - 10,y)
    frosty.dot()
    frosty.goto(x,y -10)
    frosty.dot()
    frosty.goto(x -15,y -25)
    frosty.down()
    frosty.forward(30)
    frosty.up()
    
# A function for drawing a snowman arm with 2 fingers
#  by supplying the x,y coordinate
#  as well as the lenght of the arm and angle of the arm
def Arm(x,y,length,heading):
    frosty.up()
    frosty.goto(x,y)
    frosty.setheading(heading)
    frosty.down()
    frosty.forward(length)
    frosty.setheading(heading + 20)
    frosty.forward(20)
    frosty.up()
    frosty.back(20)
    frosty.down()
    frosty.setheading(heading - 20)
    frosty.forward(20)
    frosty.up()
    frosty.home()

# A function for drawing a circle by supplying the radius and y coordinate
def Circle(radius,y):
    frosty.up()
    frosty.sety(y)

    # arc length = deg of arc * (pi/180) * radius
    arc_length = 1 * (math.pi/180) * radius
    
    frosty.down()
    
    frosty.begin_fill() #fill circle after it is drawn
    # itterate by making a bunch of little lines to form a circle
    for i in range(360):
        frosty.forward(arc_length)
        frosty.left(1)
    frosty.up()
    frosty.end_fill()
    
# call all functions to create a snowman
Circle(40,20)    #head
Circle(70,-120)  #upper torso
Circle(100,-320) #lower torse
Arm(70,-50,50,20) #right arm
Arm(-70,-50,50,160) #left arm
Face(0,70) # the face

screen.exitonclick()
