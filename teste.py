service = int(input('Type your time of service: '))
wage = float(input('Type your wage: '))
if service >10:
    print(f'its increase was {wage*0.20}')
elif 5 >= service <=10:
    print(f'its increase was {wage*0.10}')
else:
    print(f'its increase was {wage*0.05}')