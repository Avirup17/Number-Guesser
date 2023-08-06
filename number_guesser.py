import random

attempt=1

def close():
    print('Dissapointed to see that!!')
    print('Thanks for your valuable time')
    
def guess(number):
    global attempt
    random_number=random.randint(1,9)
    if((number<1)or(number>9)):
        print('Please guess a number between 1-9')
        print('----------------------------------')
        print('----------------------------------')
        start_game()
        
    else:
        if(number==random_number):
            print('Well Done!!')
            print('---------------------------------------')
            print('You WON the game in ',attempt,' attempt')
            print('---------------------------------------')
            print('Want to play 1 more round ??')
            print(' ')
            ready()
            
        else:
            attempt=attempt+1
            print('Better Luck Next Time')
            print(' ')
            print('The lucky number was ',random_number)
            print('------------------------------')
            print('------------------------------')
            print('       Lets TRY AGAIN')
            print('      *****************')
            start_game()

def start_game():
        number=int(input('Enter your number = '))
        print('------------------------------')
        print('Your number = ',number)
        print('------------------------------')
        guess(number)

def ready():
    print('Are you ready(Y/N)??')
    print(' ')
    option=input('Your Answer : ')
    print('------------------------------')
    if(option.lower()=='y'):
        start_game()
    elif(option.lower()=='n'):
        close()
    else:
        print('WRONG INPUT')
        print(' ')
        ready()

print('     Hello Explorer')
print('     **************')
print('Lets check your luck Today!!!')
print('------------------------------')
ready()
