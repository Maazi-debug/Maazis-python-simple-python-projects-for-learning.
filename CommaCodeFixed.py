# A program that takes a list and prints it out in strings,
# seperated by commas with an "and" inserted before the last item


# My first program for the problem (made by myself)
#def printer(LIST):

    #LIST.insert(3, 'and')
    #print(f'{LIST[0]}, {LIST[1]}, {LIST[2]} {LIST[3]} {LIST[4]}')


#spam = ['apples', 'bananas', 'tofu', 'cats']
#printer(spam)


# My second program, which is better but not completely right (made by myself)

#def printer(LIST):
    #LIST.insert(-1, 'and')
    #for i in (LIST):
      #  print(i, end=', ')



#spam = ['apples', 'bananas', 'tofu', 'cats']
#printer(spam)

# My third (with the help of gemini!)

def printer(LIST):
    if len(LIST) >= 1:
        LIST.insert(-1, 'and')
    else:
        LIST = []

    for index, item in enumerate(LIST):
        if index == len(LIST) - 1:
            print(item)

        elif item == 'and':
            print(item, end=' ')

        else:
            print(item, end=', ')


spam = ['apples', 'bananas', 'tofu', 'cats']
printer(spam)
