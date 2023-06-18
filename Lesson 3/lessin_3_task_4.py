import turtle 
 
# Set up the Turtle screen 
screen = turtle.Screen() 
screen.setup(500, 500) 
screen.title("Draw a Cat") 
 
# Create a new Turtle object 
cat = turtle.Turtle() 
 
# Draw the head 
cat.penup() 
cat.goto(0, 100) 
cat.pendown() 
cat.circle(50) 
 
# Draw the ears 
cat.penup() 
cat.goto(-40, 160) 
cat.pendown() 
cat.circle(10) 
cat.penup() 
cat.goto(40, 160) 
cat.pendown() 
cat.circle(10) 
 
# Draw the eyes 
cat.penup() 
cat.goto(-20, 120) 
cat.pendown() 
cat.dot(10) 
cat.penup() 
cat.goto(20, 120) 
cat.pendown() 
cat.dot(10) 
 
# Draw the nose 
cat.penup() 
cat.goto(0, 100) 
cat.pendown() 
cat.setheading(270) 
cat.circle(15, -180) 
 
# Draw the mouth 
cat.penup() 
cat.goto(-40, 100) 
cat.pendown() 
cat.setheading(270) 
cat.circle(15, -180) 
 
# Hide the Turtle object 
cat.hideturtle() 
 
# Exit on click 
turtle.exitonclick()