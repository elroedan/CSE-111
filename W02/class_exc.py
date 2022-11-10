# print('object', 20, sep = 'am', end = 'how old are you? ', flush = True)

# import math
# def random_math():
#     x = (math.ceil(math.pow(17,9) / 3) - 6 )
#     return x % 2 == 0 
# print(random_math())
  
# import a random package and make a list of random numbers ... sort it from smallest to largest
# import random
# x = []
# for y in range(0,5):
#     n = random. randint(1, 30)
#     x .append(n)
# x.sort()
# print(x)
from datetime import datetime

now = datetime.now()

display_message = 'Even Message'
if now % 2 == 0:
    print('Even')
else: 
    print('Odd')