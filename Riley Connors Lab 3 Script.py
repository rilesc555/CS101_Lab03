print('Welcome to the Flarsheim Guesser!')
print()
repeat = 'y'

#checks for integer or float input
def check(user_input):
    try:
        int(user_input)
        return True
    except:
        try:
            float(user_input)
            return True
        except:
            return False

repeat = 'y'

while repeat == 'y' or repeat == 'Y':
    print('Please think of a number between and including 1 and 100')
    print()
    #gets remainders and checks each for integer and correct range
    rem3 = input('What is the remainder when your number is divided by 3?\n')
    while check(rem3) == False:
        rem3 = input('Invalid input. Please enter an integer\n')
    else:
        rem3 = int(rem3)
        while rem3 < 0 or rem3 > 2:
            rem3 = input('The value entered must be between 0 and 2\n')
            while check(rem3) == False:
                rem3 = input('The value entered must be between 0 and 2\n')
            else:
                rem3 = int(rem3)
    print()
    rem5 = input('What is the remainder when your number is divided by 5?\n')
    while check(rem5) == False:
        rem5 = input('Invalid input. Please enter an integer\n')
    else:
        rem5 = int(rem5)
        while rem5 < 0 or rem5 > 4:
            rem5 = input('The value entered must be between 0 and 4\n')
            while check(rem5) == False:
                rem5 = input('The value entered must be between 0 and 4\n')
            else:
                rem5 = int(rem5)
    print()
    rem7 = input('What is the remainder when your number is divided by 7?\n')
    while check(rem7) == False:
        rem7 = input('Invalid input. Please enter an integer\n')
    else:
        rem7 = int(rem7)
        while rem7 < 0 or rem7 > 6:
            rem7 = input('The value entered must be between 0 and 6\n')
            while check(rem7) == False:
                rem7 = input('The value entered must be between 0 and 6\n')
            else:
                rem7 = int(rem7)

    
    print()
    for i in range(1,101):
        if i % 3 == rem3:
            if i % 5 == rem5:
                if i % 7 == rem7:
                    print(f'Your number was {i}')
                else:
                    pass
            else:
                pass
        else:
            pass
    print('How amazing is that?!')

    repeat = input('Do you want to play again? Y to continue, N to quit: ')
    while repeat not in ['Y', 'y', 'N', 'n']:
        repeat = input('Do you want to play again? Y to continue, N to quit: ')
    print()

     
    

    

    


    

        
    
