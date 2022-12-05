import turtle

width = 700
height = 600
delay = 400 #Milli second


screen = turtle.Screen()
screen.setup(width, height)
screen.title("Yo! Mr. White")

screen.bgcolor('yellow')
screen.tracer(0) # Turn off automatic animation


my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('black')

my_turtle.penup()

snake = [[0,0], [20,0], [40, 0], [60, 0]] 

for segment in snake:
    my_turtle. goto(segment[0], segment[1])
    my_turtle.stamp()

x=10
while x == 10:
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(100)
    my_turtle.right(60)
    my_turtle.forward(50)
    my_turtle.right(90)
    
    my_turtle.forward(50)
    my_turtle.right(90)
    
    my_turtle.forward(50)
    my_turtle.right(90)
 
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    my_turtle.forward(50)
    my_turtle.right(90)
    

turtle.done()
