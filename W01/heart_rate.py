"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
print('Welcome to rate my heart program!')
person = input('What is your name? ')
old = int(input(f'How old are you {person}? '))

calculate = 220 - old 
maximum = calculate * .85
minimum = calculate * .65
 
print(f'When you exercise to strengthen your heart, you should\n\
keep your heart rate between {minimum:.2f} and {maximum:.2f} beats per minute.')
