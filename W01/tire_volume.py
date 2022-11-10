from datetime import datetime
import math

print()

tire_width = float(input('Enter the width of the tire in mm (ex 205): '))
tire_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))    
wheel_diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

current_date = datetime.now()
volume = (math.pi * (tire_width)**2 * tire_ratio) * \
((tire_width * tire_ratio) + (2540 * wheel_diameter))

print(f'The appoximate volume is {(volume/10000000000):.2f} liters')

purchase = input('Would you like to buy the tires with the dimensions you entered? ').lower()

if purchase == 'yes':
    phone_number = input('What is your phone number? ')
    with open('volumes.txt', 'at') as file:
        file.write(f'{current_date: %Y-%m-%d}, {tire_width:g}, {tire_ratio:g}, {wheel_diameter:g}, {(volume/10000000000):.2f}, {phone_number}\n' )
        print(file)
else:
    with open('volumes.txt', 'at') as file:
        file.write(f'{current_date: %Y-%m-%d}, {tire_width:g}, {tire_ratio:g}, {wheel_diameter:g}, {(volume/10000000000):.2f}\n' )
        print(file)
    

