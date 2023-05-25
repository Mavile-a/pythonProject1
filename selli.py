user = int(input('-->'))
print(type(user))

if user < 6:
    print('Where are your parents?')
elif user < 16:
    print('This is a movie for adults!')
elif user > 65:
    print('Show your pension certificate!')
elif '7' in 'user':
    print('You will be lucky!')
else:
    print('There are no more tickets!')