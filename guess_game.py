import game_modules as g
from time import sleep

print("$" * 41)
print("Hello and Welcome to Number Guessing Game")
print("$" * 41)

sleep(1)
print("-" * 41)
sleep(3)

print('''
    Some rules of the Game:
    Select Difficulties level
    1. Easy to enter even numbers between the range of 1 - 20
    2. Intermediate: to enter odd number between the range of 1 - 20
    3. Hard: to guess prime number between the range of 1 - 20
    
    In the Game you are only allow maximum guesses of 6:
    if guess  == random number, the game breaks and u take your win
    else guess != random number, you'll continue until you exceed your total number of guess
''')

sleep(20)
g.start()
msg = 'Sorry try again!'

try:
    def game():
        level = input('Enter Level: (1, 2, 3): ')
        if level in ('1', '2', '3'):
            if level == '1':
                print(f'{level} - Easy was selected, enter even numbers between the range of 1 - 20\n'
                      f'clue: 2, 4, 6, 8, 10, 12, 14, 16, 18')

            elif level == '2':
                print(f'{level} - Intermediate was selected: enter odd number between the range of 10 - 40\n'
                      f'clue: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,\n'
                      f'25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49')

            else:
                print(f'{level}: Hard was selected: guess prime number between the range of 1 - 20\n'
                      f'clue: 3, 5, 7, 9, 11, 13, 15, 17, 19')

            while g.guess_count < 6:
                guess = int(input('Take a guess: '))
                if level == '1':
                    g.easy()
                    g.guess_count += 1
                    if guess == g.easy():
                        print(f'Congrats! you win with Guess-count of : {g.guess_count}')
                        g.result = 'true'
                        break

                    elif guess != g.easy():
                        print(f'You Guessed: {guess}')
                        print(f'machine_Guess: {g.easy()}')
                        print(f"{msg} and Guess-count of: {g.guess_count}")

                elif level == '2':
                    g.intermediate()
                    g.guess_count += 1
                    if guess == g.intermediate():
                        print(f'Congrats! you win with Guess-count of : {g.guess_count}')
                        g.result = 'true'
                        break

                    elif guess != g.intermediate():
                        print(f'You Guessed: {guess}')
                        print(f'machine_Guess: {g.intermediate()}')
                        print(f"{msg} and Guess-count of: {g.guess_count}")

                elif level == '3':
                    g.hard()
                    g.guess_count += 1
                    if guess == g.hard():
                        print(f'Congrats! you win with Guess-count of : {g.guess_count}')
                        g.result = "true"
                        break

                    elif guess != g.hard():
                        print(f'You Guessed: {guess}')
                        print(f'machine_Guess: {g.hard()}')
                        print(f"{msg} system guess {g.hard()} and Guess-count of: {g.guess_count}")

        elif g.guess_count == 6:
            print('You have reach your guess limit, game exiting')

        else:
            print('invalid parameter! out of range')


    game()
except KeyboardInterrupt as err:
    err = 'User interrupted by pressing ctl + c'
    print(err)

except ValueError as err:
    err = "Invalid value entered"
    print(err)
