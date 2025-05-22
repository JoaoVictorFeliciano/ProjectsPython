password = input('Type your password: ')

error=[]
if len(password) <8:
    error.append('The password must have 8 characters.')

if not any(char.islower() for char in password):
    error.append('The password must contain at least one lowercase letter.')

if not any(char.isupper() for char in password):
    error.append('The password must contain ate least one uppercase letter.')

if not any(char.isdigit() for char in password):
    error.append("The password must have a one number.")

if len(error) == 0:
    print('Valid Password')
else:
    print('Invalid Password, fix the folowwing issues.')
    for erro in error:
        print('-', erro)