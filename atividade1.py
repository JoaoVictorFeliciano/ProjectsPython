nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))

print ('Categoria A: Iniciante- R$58,00 \nCategoria B: Intermediário- R$70,00 \nCategoria C: Avançado- R$81,00')

categoria = input("Digite a categoria do curso (A - Iniciante, B - Intermediário, C - Avançado): ").upper()
if categoria == 'A':
    mensalidade = 58.00
elif categoria == 'B':
    mensalidade = 70.00
elif categoria == 'C':
    mensalidade = 81.00 

select = input('Deseja ter o material incluso? (S, N): ').upper()

if select == 'S':
    material = (mensalidade*0.15)
else:
    material = 0.0

mensalidade_total = mensalidade+material

print(f'Nome do aluno: {nome} \nCategoria: {categoria} R${mensalidade} \nMaterial incluso:{'Sim' if  select == 'S' else 'Não'}')
if material >0:
    print(f'Valor do material:{material}')
print(f'Valor Total da mensalidade:{mensalidade_total}')
