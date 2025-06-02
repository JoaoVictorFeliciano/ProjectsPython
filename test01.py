while True:
    sum = 0
    counter = 0
    while counter < 3:
        notes = int(input('Type your notes: '))
        sum += notes
        counter += 1
    media = sum / 3

    if media >= 7:
        print('Aprovved your media is: ', media)
    elif 4 <= media <= 6:
        print('Recuperation your media is: ', media)
    elif media <= 0:
        print('Type your notes again')
    else:
        print('Failed your media is: ', media)

    keep = input('Do you want to calculate another average? (y/n) ')
    if keep.lower() != 'y':
        print('Program closed.')
        break


