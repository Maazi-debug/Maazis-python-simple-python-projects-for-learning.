# A program where you are given a list,
# And then you have to acces the third element,
# You need to count the amount of items
# And you should also check if that list is empty


# Feel free to change the list, to bug test this program

number = [1, 2, 3, 4, 5, 6]

#number = ["]
#number = []

# Here it says if the list value in number is less than three it will print that
# Item nr. 3 is not there since there isn't even a third item
# But if there were to be three items it will just print the third item in the list
if len(number) < 3 :
    print('Item three is: There is not an item three in the list "number"')

else:
    print('Item three is:', number[2]) # number[2:3]

# The len function counts the amount of items in a list
print('The totat item amount is:', len(number))

# If the list has one item or more it will say that list is not empty.
# Then if its not true that the list value is less than one which is zero, it will print list is empty
if len(number) >= 1:
    print('List is not empty')

else:
    print('List is empty')
