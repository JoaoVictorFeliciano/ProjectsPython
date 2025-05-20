idade=int(input('Digite sua idade: '))

if idade < 16:
    print('Você não é eleitor.')
elif 18 <= idade < 65:
    print('Eleitor Obrigatório.')
else:
    print('Eleitor Facultativo')
if idade == 18:
    sexo=input('Digite seu sexo (M , F)').upper()
    if sexo == 'M':
        print('Lembre do seu Alistamento Militar.')
    else:
        print('Você não precisa do Alistamento Militar.')
