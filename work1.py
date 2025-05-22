buy = int(input('Type the purchase value: '))
if buy <=100:
    print('No discount')
elif buy <=500:
    discount= buy*0.10
elif buy <=1000:
    discount= buy*0.15
elif buy >1000:
    discount= buy*0.20

final_value= buy - discount

print(f'The discount is {discount:.2f}')
print(f'The final value is {final_value:.2f}')