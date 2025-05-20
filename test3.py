password_correct = '140714'
attemps = 0
max_attemps = 3
while attemps < max_attemps:
    password = input('Type a password: ')

    if password == password_correct:
        print('Access Granted')
        break
    else:
        attemps += 1
        print('Password incorrect. Try again')
    
    if attemps == max_attemps:
        print('Access denied, you try 3 times and now is blocked.')