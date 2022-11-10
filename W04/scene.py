# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_pond(canvas, scene_width, scene_height)
    draw_house(canvas, scene_width, scene_height)
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
  
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill= 'sky blue')


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")

    # Draw a pine tree.
    tree_center_x = []
    tree_bottom = []
    tree_height = []
    for i in range(200):
        center_x = random.randint(50,500)
        add_x = tree_center_x.append(center_x)
        bottom = 160
        add_bottom = tree_bottom.append(bottom)
        height = random.randint(180,230)
        add_height = tree_height.append(height)

        draw_pine_tree(canvas, tree_center_x[i],
                tree_bottom[i], tree_height[i])

def draw_house(canvas, scene_width, scene_height):

    draw_rectangle(canvas, 600, scene_height/3, 790, 300, fill="brown", outline= "brown")
    draw_rectangle(canvas, 700, scene_height/3, 750, 200, fill="black", outline= "brown")
    draw_rectangle(canvas, 650, 300, 700,350, fill="grey", outline= "black" )



    # draw_polygon(canvas, 600, 300, 790, 500,outline="gray20", width=1, fill="brown")
        
def draw_clouds(canvas, scene_width, scene_height):

    x = 110
    while x != 0:
        draw_oval(canvas, 100 + x, 400 , 200, 450, fill = "white", outline="white")
        x -= 1
    y = 40
    while y != 0:
        draw_oval(canvas, 100 + y , 400 , 200, 490, fill = "white", outline="white")
        y -= 1
    x = 110
    while x != 0:
        draw_oval(canvas, 300 + x, 400 , 400, 450, fill = "white", outline="white")
        x -= 1
    y = 40
    while y != 0:
        draw_oval(canvas, 300 + y , 400 , 400, 490, fill = "white", outline="white")
        y -= 1
        
def draw_pond(canvas, scene_width, scene_height):
    y = 40
    while y != 0:
        draw_oval(canvas, 100 + y , 20 , 790, 130, fill = "dark blue", outline="dark blue")

        y -= 1

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()