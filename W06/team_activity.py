rates = []
score = 0

def main():

    purpose_program()
    choice_points()
    print('1. I feel that I am a person of worth, at least on an\n\
equal plane with others.')
    rate_1 = input('Enter D, d, a, or A: ')
    rates.append(rate_1)
    print('2. I feel that I have a number of good qualities.')
    rate_2 = input('Enter D, d, a, or A: ')
    rates.append(rate_2)
    print('3. All in all, I am inclined to feel that I am a failure.')
    rate_3 = input('Enter D, d, a, or A: ')
    rates.append(rate_3)
    print('4. I am able to do things as well as most other people.')
    rate_4 = input('Enter D, d, a, or A: ')
    rates.append(rate_4)
    print('5. I feel I do not have much to be proud of.')
    rate_5 = input('Enter D, d, a, or A: ')
    rates.append(rate_5)
    print('6. I take a positive attitude toward myself.')
    rate_6 = input('Enter D, d, a, or A: ')
    rates.append(rate_6)
    print('7. On the whole, I am satisfied with myself.')
    rate_7 = input('Enter D, d, a, or A: ')
    rates.append(rate_7)
    print('8. I wish I could have more respect for myself.')
    rate_8 = input('Enter D, d, a, or A: ')
    rates.append(rate_8)
    print('9. I certainly feel useless at times.')
    rate_9 = input('Enter D, d, a, or A: ')
    rates.append(rate_9)
    print('10. At times I think I am no good at all.')
    rate_10 = input('Enter D, d, a, or A: ')
    rates.append(rate_10)
    
    print(score_rating(rates, score))

def purpose_program():
    print('This program is an implementation of the Rosenberg\n\
Self-Esteem Scale. This program will show you ten\n\
statements that you could possibly apply to yourself.\n\
Please rate how much you agree with each of the\n\
statements by responding with one of these four letters:')

def choice_points():
    print('D means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.')

def score_rating(rates, score):

    for i in range(10):
        if rates[i] == 'A':
            score += 3
            
        elif rates[i] == 'a':
            score += 2
        elif rates[i] == 'd':
            score += 1
        elif rates[i] == 'D':
            score += 0
    print(f'Your score is: {score}')    

# def compute_total():
#     pass

main()