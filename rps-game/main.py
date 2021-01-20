from random import randint

styles = ['rock','paper','scissor']
print('Pick your style:\n')
for no, style in enumerate(styles):
    print(str(no + 1) + '. ' + style.capitalize())
while True:
    # Get computer random style 
    computer = randint(0,2)
    try:
        # Get user style
        user = int(input('>>> ')) - 1
        if isinstance(user, int) and user < 3:
            if computer == 0 and user == 1:
                print('You win!')
            elif computer == 0 and user == 2:
                print('You lose!')
            elif computer == 1 and user == 2:
                print('You win!')
            elif computer == 1 and user == 0:
                print('You lose!')
            elif computer == 2 and user == 0:
                print('You win!')
            elif computer == 2 and user == 1:
                print('You lose!')
            else:
                print('Draw')

            print('Computer: ' + styles[computer].capitalize())
            print('User\t: ' + styles[user].capitalize())
    except (ValueError, IndexError):
        print('Value must be valid int [1-3]')
