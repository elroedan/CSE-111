import turtle

width = 700
height = 600
delay = 10


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, delay)

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Yo! Mr. White")
screen.bgcolor('yellow')
screen.tracer(0)

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('black')

move_turtle()

turtle.done()