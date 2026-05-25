import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    some_list = []
    for i in range(100):
        if random.randint(0, 1) == 'H':
            some_list.append('H')
        else:
            some_list.append('T')


    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(len(some_list) - 5):
        some


print('Chance of streak: %s%%' % (number_of_streaks / 100))
