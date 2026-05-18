# An example of try-except paired with a raise statement

def figure(height, width):
    if height > 10:
        raise Exception('Height must not exceed past 10!')

    if width < 2:
        raise Exception('Are you trying to look like a skeleton, if i may ask?')

    for i in range(1, 5):
        print('*' * height)
        print(width * '*' + width * '*')
        print('*' * height)


try:
    figure(10, 5)

except Exception as errors:
    print('Something went wrong: ' + str(errors))

try:
    figure(5, 2)

except Exception as errors:
    print('Something went wrong: ' + str(errors))
