import math
items = int(input('Enter the number of items: '))
boxes = int(input('Wnter the number of items per box: '))
x = math. ceil(items/boxes) 
print(f"For {items}, packing {boxes} in each box, you will need {x} boxes. ")


# > python boxes.py
# Enter the number of items: 8
# Enter the number of items per box: 5

# For 8 items, packing 5 items in each box, you will need 2 boxes.
