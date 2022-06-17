print("""
Este quiz foi desenvovildo com a finalidade de treinar programação.
Abaixo, encontrará uma série de perguntas, e um campo de digitação para sua resposta.
Analise as perguntas e escolha a alternativa certa e envie sua resposta. 

- Editor
""")
print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '3', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 9?',
        'respostas': {'a': '26', 'b': '28', 'c': '27', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 3 - 6?',
        'respostas': {'a': '-2', 'b': '0', 'c': '-3', },
        'resposta_certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 9 / 3?',
        'respostas': {'a': '2', 'b': '3', 'c': '4', },
        'resposta_certa': 'b',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 3 + 9 * 2?',
        'respostas': {'a': '21', 'b': '24', 'c': '22', },
        'resposta_certa': 'a',
    },
    'Pergunta 6': {
        'pergunta': 'Quanto é x? x = (8 + 3) + (4 * 2)',
        'respostas': {'a': '18', 'b': '20', 'c': '19', },
        'resposta_certa': 'c',
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Alternativas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Resposta:')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns, você acertou!')
        respostas_certas += 1
    else:
        print('Que pena, você errou!')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = (respostas_certas / qtd_perguntas) * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
print()
