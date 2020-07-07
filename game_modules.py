import random as r

guess_count = 0
result = 'false'


def easy():
    even = []
    for num in range(1, 20):
        if num % 2 == 0:
            even.append(num)
    even_gen = r.choice(even)
    return even_gen


def intermediate():
    odd = []
    for num in range(1, 50):
        if num % 2 != 0:
            odd.append(num)

    odd_gen = r.choice(odd)
    return odd_gen


def hard():
    prime = []
    for num in range(10, 40, + 1):
        if num > 1:
            for x in range(2, num):
                if num % x == 0:
                    break
                else:
                    prime.append(num)

    prime_gen = r.choice(prime)

    return prime_gen


def start():
    new_guess = input(''' Ready to start? \n Please enter Y for YES and N for No:  ''')
    if new_guess.upper() == 'Y':
        print('''
        Fasting your seat belt and Game begins now....
        ''')
    else:
        print('Thanks for stopping by.')
