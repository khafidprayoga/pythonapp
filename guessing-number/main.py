from random import randint

number = randint(0,7) # Generate random int number from 0 to 7
print('I have random number from 0 to 7')
print('Guess it !')

while True:
    try:
        # Get valid type data (int)
        user_num = int(input('>>>  '))
    except ValueError as err:
        # Print if user input another type data
        print('Please input valid int number')
    else:
        if user_num > 7:
            print('My number is between 0 and 7')
        else:
            if user_num != number:
                if number > user_num:
                    print('My random number is greater than your number')
                elif number < user_num:
                    print('My random number is lower than your number')
            elif user_num == number:
                print('Got it, you are right!')
                break
            