# A quiz on animals
apple = 0
while apple < 1:
    print('Hello fellow welcome to this game of guess the animal!')

    # Here i am asking questions and i use answer as my variable name to fact check them
    print('1. question: what animal is known for laughing and often ganging up on lions?')
    answer = input('>')

    if answer == 'Hyena' or answer == 'hyena':
        print('Correct!')
    else:
        print('Wrong it was a hyena!')

    print('2. question: what animal is known to be closest to the human species. a) Dolphin b) Elephant c) Chimpanze ')
    answer_1 = input('>')

    if answer_1 == 'C' or  answer_1 == 'c':
        print('Correct!')
    else:
        print('Wrong it was a chimpanzee!')

    print('3. question: what is known as the fastet animal on earth. a) Gorilla b) Cheetah c) The peregrine falcon ')
    answer_2 = input('>')
    if answer_2 == 'C' or answer_2 == 'c':
        print('Correct!')

    else:
        print('Wrong it was The peregine falcon!')

    print('Thank you for playing the game on guess on the animal!')

    apple = apple + 2

