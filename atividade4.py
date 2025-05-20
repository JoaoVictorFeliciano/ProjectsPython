valor=float(input('Digite o valor da casa: '))
salario=float(input('Digite o seu sálario mensal: '))
anos=int(input('Digite a quantidade de anos para pagar a casa: '))
meses= anos*12
mensal= valor/meses
limite_max= salario *0.30
if mensal <= limite_max:
    print("\nEmpréstimo APROVADO!")
else:
    print("\nEmpréstimo NEGADO!")
    print("A prestação excede 30% do seu salário mensal.")

print(f"Valor da prestação: R$ {mensal:.2f}")
print(f"Limite máximo (30% do salário): R$ {limite_max:.2f}")

