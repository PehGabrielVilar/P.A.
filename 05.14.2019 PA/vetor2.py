notas = []
notas.append (eval(input('Digite a nota do primeiro aluno: ')))
notas.append (eval(input('Digite a nota do segundo aluno: ')))
notas.append (eval(input('Digite a nota do terceiro aluno: ')))
print (notas)

media = 0

for i in range (3):
    media = media + notas [i]

media = media / 3

print (media)
