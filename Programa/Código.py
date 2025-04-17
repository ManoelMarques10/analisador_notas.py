from time import sleep  # Importa a função sleep para pausar a execução por alguns segundos


# Função que recebe qualquer quantidade de notas e calcula estatísticas
def notas(*notas):
    # Dicionário que armazenará o resumo das notas
    resumo = {
        'quantidade_de_notas': 'x',
        'maior': 'x',
        'menor': 'x',
        'média': 'x',
        'situação': 'x'
    }

    # Calcula a média das notas, arredondada para 2 casas decimais
    média = round(sum(notas) / len(notas), 2)

    # Encontra a maior e menor nota
    maior = max(notas)
    menor = min(notas)

    # Conta quantas notas foram informadas
    quantidade_de_notas = len(notas)

    # Armazena os valores calculados no dicionário
    resumo['média'] = média
    resumo['maior'] = maior
    resumo['menor'] = menor
    resumo['quantidade_de_notas'] = quantidade_de_notas

    # Define a situação com base na média
    if média >= 7:
        situacao = 'Boa'
    else:
        situacao = 'Ruim'

    resumo['situação'] = situacao

    # Exibe o resumo com pequena pausa
    print('\33[37mGerando...')
    sleep(0.5)
    print(f'\33[34m{resumo}')


# Loop principal do programa
parar = 'n'
while parar != 's':
    # Recebe as notas do usuário, separadas por espaço
    entrada = input('\33[33mDigite as notas da turma (separadas por espaço): ')
    try:
        # Converte a entrada para uma lista de floats (números com vírgula)
        lista_notas = list(map(float, entrada.split()))

        # Verifica se a lista está vazia
        if not lista_notas:
            print('\33[31mVocê não digitou nenhuma nota.')
            continue

        # Chama a função passando as notas como argumentos
        notas(*lista_notas)

    except ValueError:
        # Trata erros caso o usuário digite algo inválido
        print('\33[31mOps, algo deu errado, só são aceitos números nesse programa.')

    # Pergunta se o usuário quer encerrar o programa
    parar = input('\33[36mDeseja parar? [S] ou [N] ').strip().lower()

# Mensagem final de encerramento
sleep(0.25)
print('\33[35mEncerrando... até mais.')