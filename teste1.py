import os

arquivo = "Banco de Dados.txt"

# Função para adicionar treinos

def novoTreino():
    data = input("Em que dia foi feito seu treino: dia/mês/ano ")
    tipoTreino = input("O que você treinou ? (AMRAP/EMOM/FOR TIME) ")
    tempo = input("Quanto tempo durou o seu treino: (em minutos) ")
    movimentos = input("Quais movimentos tiveram no treino: ")

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf8") as dados:
            linhasExistentes = dados.readlines()
            numero = len(linhasExistentes)
    else:
        numero = 0

    with open(arquivo, "a", encoding="utf8") as dados:
        dados.write(f"{numero} - {data}; {tipoTreino}; {tempo}; {movimentos}\n")

    print("O seu treino foi adicionado!")

# Função para visualizar treinos
def listarTreino():
    with open(arquivo, "r", encoding="utf8") as dados:
        conteudo = dados.readlines()
        if conteudo == "":
            print("Você ainda não tem nenhum treino registrado.")
        else:
            print("Aqui estão os treinos que você tem registrado:")
            for linha in conteudo:
                print(linha.strip())

# Função para editar treino
def editarTreino():
    listarTreino()
    substituicao = int(input("Qual treino você quer editar? "))
    with open(arquivo, "r", encoding="utf8") as dados:
        treinos = dados.readlines()
    
    if 0 <= substituicao < len(treinos):
        data = input("Substitua a data caso necessário: [dia/mês/ano] ")
        tipoTreino = input("Substitua o tipo de treino caso necessário: ")
        tempo = input("Substitua o tempo caso necessário: (em minutos) ")
        movimentos = input("Substitua os movimentos caso necessário: ")
        treinos[substituicao] = f"{substituicao} - {data}; {tipoTreino}; {tempo}; {movimentos}\n"

        with open(arquivo, "w", encoding="utf8") as dados:
            dados.writelines(treinos)
        print("O seu treino foi atualizado!")
    else:
        print("Índice inválido.")

# Função para excluir treino
def excluirTreino():
    listarTreino()
    numeroTreino = int(input("Qual treino você quer excluir? "))
    with open(arquivo, "r", encoding="utf8") as dados:
        treinos = dados.readlines()

    if 0 <= numeroTreino < len(treinos):
        treinos.pop(numeroTreino)
        treinos = [f"{i} - " + linha.split(" - ", 1)[1] for i, linha in enumerate(treinos)]

        with open(arquivo, "w", encoding="utf8") as dados:
            dados.writelines(treinos)
        print("Treino excluído com sucesso!")
    else:
        print("Índice inválido.")

# Menu principal
while True:
    print("-------------------------------- ")
    print("---------- WOD TRACKER ---------")
    print("-------------------------------- ")

    print("A wod tracker permite que você possa adicionar/visualizar/editar/excluir registros do seu treino de CrossFit.")
    print("Digite 1, caso queira adicionar.")
    print("Digite 2, caso queira visualizar.")
    print("Digite 3, caso queira editar.")
    print("Digite 4, caso queira excluir.")
    escolha = int(input())

    if escolha == 1:
        novoTreino()
    elif escolha == 2:
        listarTreino()
    elif escolha == 3:
        editarTreino()
    elif escolha == 4:
        excluirTreino()
    else:
        print("Opção inválida.")
