#!/usr/bin/env python

import random

def menu():
    # Ask player for number_csv
    # Calculate lottery numbers
    # Print out the winnings

    lottery_numbers = create_lottery_numbers()
    winning_numbers = get_player_numbers().intersection(lottery_numbers)

    pick_str = ' '.join([str(num) for num in lottery_numbers])
    wins_str = ' '.join([str(num) for num in winning_numbers])

    print('Winning numbers are: {}'.format(pick_str))
    print('Your winning numbers: {}'.format(wins_str))

# User can pick 6 numbers
def get_player_numbers():
    number_csv = input('Enter your 6 numbers, separated by commas:')

    number_list = number_csv.split(',')
    integer_set = {int(number) for number in number_list}
    return integer_set

def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

menu()
