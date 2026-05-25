# A program that flips a coin 10 000 times

#import random
#number_of_streaks = 0

#for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    #some_list = []
    #for i in range(101):
        #random.randint(0,1)
        #if random.randint(0,1) == 0:
            #some_list.append('T')
       # else:
            #some_list.append('H')

    # Code that checks if there is a streak of 6 heads or tails in a row
    #while len(some_list) != 101:
       # if some_list == ['H', 'H', 'H', 'H', 'H', 'H'] or ['T', 'T', 'T', 'T', 'T', 'T']:
            #number_of_streaks += 1


#print('Chance of streak: %s%%' % (number_of_streaks / 100))

# A 100 flips
import random
some_list = []
for i in range(95):
    if random.randint(0,1) == 0:
        some_list.append('T')
    else:
        some_list.append('H')

print(some_list)

# streak checker

has_streak = False

for i in range(95): # 100 - 6 + 1
    chunck = some_list[i:i+6]


    if chunck == ['H'] * 6 or chunck == ['T'] * 6:
        has_streak = True
        break


print(some_list)
print('Streak found:', has_streak)
