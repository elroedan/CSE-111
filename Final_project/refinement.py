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
def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction('up'), ('Up'))
    screen.onkey(lambda: set_snake_direction('down'), ('Down'))
    screen.onkey(lambda: set_snake_direction('left'), ('Left'))
    screen.onkey(lambda: set_snake_direction('right'), ('Right'))

def set_snake_direction(direction):
    global snake_direction
    if direction == 'up':
        if snake_direction != 'down': # No self collision simply by pressing wrong key
            snake_direction = 'Up'
    elif direction == 'down':
        if snake_direction != 'up': # No self collision simply by pressing wrong key
            snake_direction = 'Down'
    elif direction == 'left':
        if snake_direction != 'right': # No self collision simply by pressing wrong key
            snake_direction = 'Left'
    elif direction == 'right':
        if snake_direction != 'left': # No self collision simply by pressing wrong key
            snake_direction = 'Right'


def game_loop():
    stamper.clearstamps() # Remove existing stamps made by stamper


    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < -width/2 or new_head[0] > width /2\
        or new_head[1] < -height / 2 or new_head[1] > height / 2:
        main()
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
        return True
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

def main():
    global score, snake, snake_direction, food_pos
    score = 0 
    snake = [[0,0], [20,0], [40, 0], [60, 0]] 
    snake_direction = 'Up'
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()
    

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Yo! Mr. White")

    screen.bgcolor('black')
    screen.tracer(0) # Turn off automatic animation

    # Event handlers
    screen.listen()
    bind_direction_keys()


    stamper = turtle.Turtle()
    stamper.shape('square')
    stamper.color('yellow')

    stamper.penup()

    snake = [[0,0], [20,0], [40, 0], [60, 0]] 

    snake_direction = 'Up'
    score = 0



    # Food
    food = turtle.Turtle()
    food.shape('circle')
    food.color('white')
    food.shapesize(food_size /20)
    food.penup()
    food_pos = get_random_food_pos()
    food.goto(food_pos)

        
    main()    

    turtle.done()
