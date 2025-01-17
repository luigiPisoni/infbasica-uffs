def resumo():
    mensagem = "Samuel Harris Altman (Chicago, 22 de abril de 1985) é um empreendedor, investidor e programador estadunidense. É conhecido por ser o presidente da aceleradora Y Combinator e da OpenAI.."
    return mensagem


def doutorado():
    mensagem = "Após terminar o ensino médio, Altman estudou por dois anos na Universidade de Stanford, até desistir junto com dois amigos para focar em uma startup, a Loopt."
    return mensagem


def contribuicoes():
    mensagem = "CEO da OpenAI, criador do ChatGPT, presidente da Y Combinator, aceleradora que investe em startups."
    return mensagem


def artigos():
    mensagem = "DALL E 2: IA capaz de gerar imagens através de inputs fornecidos pelo usuário."
    return mensagem


def citacoes():
    mensagem = "Pessoas são incríveis criaturas de hábitos; Você não deve manufaturar progresso."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
