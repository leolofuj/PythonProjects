aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*20)
#print(f'A média do aluno(a) {aluno["nome"]}, foi de {aluno["média"]} e a sua situação é {aluno["situação"]}(a)')
for k, v in aluno.items():
    print(f'O(a) {k} foi {v}.')
