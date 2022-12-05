import turtle

width = 700
height = 600
delay = 100 #Milli second

offsets = {
    'Up': (0, 20),
    'Down': (0, -20), 
    'Left': (-20, 0), 
    'Right': (20, 0)
}

def go_up():
    global snake_direction
    if snake_direction != 'Down':
        snake_direction = 'Up'
def go_down():
    global snake_direction
    if snake_direction != 'Up':
        snake_direction = 'Down'
def go_left():
    global snake_direction
    if snake_direction != 'Right':
        snake_direction = 'Left'
def go_right():
    global snake_direction
    if snake_direction != 'Left':
        snake_direction = 'Right'

def move_snake():
    stamper.clearstamps() # Remove existing stamps made by stamper


    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]


    # Add new head to snake body
    snake.append(new_head)
    # Remove the last segment of snake
    snake.pop(0)

    # Draw snake for the first time
    for segment in snake:
        stamper. goto(segment[0], segment[1])
        stamper.stamp()
    
    # Refresh screen 
    screen.update()
    turtle.ontimer(move_snake, delay)

screen = turtle.Screen()
screen.setup(width, height)
screen.title("Yo! Mr. White")

screen.bgcolor('yellow')
screen.tracer(0) # Turn off automatic animation

# Event handlers
screen.listen()
screen.onkey(go_up, 'Up')
screen.onkey(go_down, 'Down')
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')


stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('black')

stamper.penup()

snake = [[0,0], [20,0], [40, 0], [60, 0]] 

snake_direction = 'Up'

for segment in snake:
    stamper. goto(segment[0], segment[1])
    stamper.stamp()

move_snake()    

turtle.done()
