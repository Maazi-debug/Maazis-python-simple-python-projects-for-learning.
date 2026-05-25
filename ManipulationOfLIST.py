# A program to demonstrate list manipulation; meaning how to modify a list

number = [100, 50, 400, 500]

print('Initial list',number)

number[1] = 200


print('200 changed to the list and 50´s place has been taken ',number)

number.append(600)

print('list with 600 added to the end of the list', number)

number.insert(2, 300)

print('List with 300 inserted at index 2', number)

number.remove(600)

print('600 removed from list', number)

del number[0]

print('index 0 in the list has been removed', number)
