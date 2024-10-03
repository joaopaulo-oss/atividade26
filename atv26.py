# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.
listaNotas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i}"))
    listaNotas.append(nota)

maior = max(listaNotas)
menor = min(listaNotas)
media = sum(listaNotas) / len(listaNotas)

print(f"""
Maior - {maior}
Menor - {menor}
Media - {media}
""")