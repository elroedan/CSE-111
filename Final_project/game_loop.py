import turtle
import random

width = 700
height = 600
delay = 100 #Milli second
food_size = 10

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

def game_loop():
    stamper.clearstamps() # Remove existing stamps made by stamper


    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < -width/2 or new_head[0] > width /2\
        or new_head[1] < -height / 2 or new_head[1] > height / 2:
        turtle.bye()
    else:
 
        # Add new head to snake body
        snake.append(new_head)

        # Check food collision
        if not food_collisions():
            snake.pop(0) # keeps the snake length same length 

        # Draw snake for the first time
        for segment in snake:
            stamper. goto(segment[0], segment[1])
            stamper.stamp()
        
        # Refresh screen 
        screen.title(f'Snake Game. Score: {score}')
        screen.update()
        turtle.ontimer(game_loop, delay)
def food_collisions():

    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-width/ 2 + food_size, width / 2 - food_size) 
    y = random.randint(-height/ 2 + food_size, height / 2 - food_size) 

    return(x, y)
def get_distance(pos1, pos2):

    x1, y1 = pos1

    x2, y2 = pos2

    distance = ((y2-y1)**2 + (x2-x1)**2) ** 0.5 # pythogoras' theorem
    return distance 

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
score = 0

for segment in snake:
    stamper. goto(segment[0], segment[1])
    stamper.stamp()

# Food
food = turtle.Turtle()
food.shape('circle')
food.color('green')
food.shapesize(food_size /20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

game_loop()    

turtle.done()
