import game_modules as g
from time import sleep

print("$" * 41)
print("Hello and Welcome to Number Guessing Game")
print("$" * 41)

sleep(1)

print("-" * 41)

sleep(1)

print('''
    Some rules of the Game:
    Select Difficulties level
    1. Easy to enter even numbers between the range of 1 - 20
    2. Intermediate: to enter odd number between the range of 10 - 40
    3. Hard: to guess prime number between the range of 1 - 50
    
    In the Game you are only allow maximum guesses of 6:
    if guess  == random number, the game breaks and u take your win
    else guess != random number, you'll continue until you exceed your total number of guess
''')

sleep(1)

g.start()

msg = 'Sorry! take a guess again'


try:
    def game():
        level = input('Enter Level: (1, 2, 3): ')
        if level in ('1', '2', '3'):
            while g.guess_count < 6:
                guess = int(input('Take a guess: '))
                if level == '1':
                    print(f'{level} was selected, enter even numbers between the range of 1 - 20')
                    g.easy()
                    g.guess_count += 1
                    if guess == g.easy():
                        print(f'Congrats! you win with count of : {g.guess_count}')
                        g.result = 'true'
                        break

                    elif guess != g.easy():
                        print(f"{msg} and count of: {g.guess_count}")

                elif level == '2':
                    g.intermediate()
                    g.guess_count += 1
                    if guess == g.intermediate():
                        print(f'Congrats! you win with count of : {g.guess_count}')
                        break

                    elif guess != g.intermediate():
                        print(f"{msg} and count of: {g.guess_count}")

                elif level == '3':
                    g.hard()
                    g.guess_count += 1
                    if guess == g.hard():
                        print(f'Congrats! you win with count of : {g.guess_count}')
                        g.result = 'true'
                        break

                    elif guess != g.hard():
                        print(f"{msg} and count of: {g.guess_count}")

        elif g.guess_count == 6:
            print('You have reach your guess limit, game exiting')

        else:
            print('invalid parameter! out of range')


    game()
except KeyboardInterrupt as err:
    print(err)

except ValueError as err:
    print(err)