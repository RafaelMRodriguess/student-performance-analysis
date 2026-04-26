import pandas as pd

df = pd.read_csv("projeto_github/dados.csv")

def tabela_completa(df):
    print('=== TABELA COMPLETA ===')
    print(df)

def media_geral(df):
    print('\n=== MEDIA GERAL DAS NOTAS ===')
    print(f"{df['nota'].mean():.1f}")

def media_por_idade(df):
    print('\n=== MEDIA DAS NOTAS POR IDADE ===')
    print(df.groupby('idade')['nota'].mean().round(1).sort_index().to_frame())

def maior_nota_por_idade(df):
    print('\n=== MAIOR NOTA POR IDADE ===')
    print(df.groupby('idade')['nota'].max().sort_index().to_frame())

def menor_nota_por_idade(df):
    print('\n=== MENOR NOTA POR IDADE ===')
    print(df.groupby('idade')['nota'].min().sort_index().to_frame())

def quantidade_alunos_por_idade(df):
    print('\n=== QUANTIDADE DE ALUNOS POR IDADE ===')
    print(df.groupby('idade')['nome'].count().sort_index().to_frame())

def quantidade_alunos_nota_alta(df):
    print('\n=== QUANTIDADE ALUNOS COM NOTA > 7 POR IDADE ===')
    print(df[df['nota'] > 7].groupby('idade')['nome'].count().sort_index().to_frame())

def alunos_nota_baixa(df):
    print('\n=== ALUNOS COM NOTA BAIXA ===')
    print(df[df['nota'] < 7])

def aluno_destaque(df):
    print('\n=== ALUNO DESTAQUE ===')
    print(df.loc[df['nota'].idxmax()])

def relatorio_geral(df):
    print('\n' + '='*40)
    print('=== RELATORIO GERAL ===')
    print('='*40)
    print()
    media_geral(df)
    print()
    media_por_idade(df)
    print()
    maior_nota_por_idade(df)
    print()
    menor_nota_por_idade(df)
    print()
    quantidade_alunos_por_idade(df)
    print()
    quantidade_alunos_nota_alta(df)
    print()
    alunos_nota_baixa(df)
    print()
    aluno_destaque(df)

print('=== SISTEMA DE ANÁLISE DE ALUNOS ===')

while True:
    print('\n[1] Tabela completa\n[2] Media geral das notas\n[3] Media das notas por idade\n[4] Maior nota por idade\n[5] Menor nota por idade\n[6] Quantidade de alunos por idade\n[7] Quantidade de alunos com nota > 7 por idade\n[8] Alunos com nota baixa\n[9] Aluno(a) destaque\n[10] Relatorio geral\n[0] Sair\n ')
    try:
        opcao = int(input('Selecione uma opção para análise: '))
    except ValueError:
        print('Digite apenas numeros!')
        continue

    if opcao == 1:
        tabela_completa(df)

    elif opcao == 2:
        media_geral(df)

    elif opcao == 3:
        media_por_idade(df)

    elif opcao == 4:
        maior_nota_por_idade(df)

    elif opcao == 5:
        menor_nota_por_idade(df)

    elif opcao == 6:
        quantidade_alunos_por_idade(df)

    elif opcao == 7:
        quantidade_alunos_nota_alta(df)

    elif opcao == 8:
        alunos_nota_baixa(df)

    elif opcao == 9:
        aluno_destaque(df)
    
    elif opcao == 10:
        relatorio_geral(df)


    elif opcao == 0:
        break

    else:
        print('Opcao invalida!')

print('Analises encerradas.')

