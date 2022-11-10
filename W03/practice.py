# # from datetime import datetime
# # # Function to print current date and time
# # def print_time(task_name):
# #     print(task_name)
# #     print(datetime.now())
# #     print()
# # # print timestamps to see how long sections of code 
# # # take to run

# # first_name = 'susan'
# # print_time('first name assigned')

# # for x in range(0,10 ):
# #     print(x)
# # print_time('loop completed')


# from webbrowser import get


# def get_initials(name):
#     initials = name[0:1].upper()
#     return initials

    

# first_name = input('Enter your first name: ')
# first_name_initial = get_initials(first_name)

# middle_name = input('Enter your middle name: ')
# middle_name_initial = get_initials(middle_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initials(last_name)

# print(f'Your initial are: {first_name_initial}{middle_name_initial}\
# {last_name_initial} ')
# def get_initial(name, force_uppercase):
#     if force_uppercase:
#         initial = name[0:1]
    
#     else: 
#         initial = name[0:1]

#     return initial

# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(force_uppercase = True, \
#     name = first_name)

# print('Your initial are: ' + first_name_initial)
import math

def compute_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

print(compute_cylinder_volume(2.5,5)) 