import os
import random

arquivo = "Banco de Dados.txt"
desempenhoTxt = "Metas.txt"

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

#Função para filtrar treinos

def filtraTreino():

    modo = input("Você quer filtrar por tipo do treino (exm:EMOM) ou por movimento (exm:snatch) ? ")

    with open(arquivo, "r",encoding="utf8") as dados:
        treinos =dados.readlines()
    
    treinosEncontrados = [linha for linha in treinos if modo.lower() in linha.lower()]

    if treinosEncontrados:
        print(f"treinos encontrados {modo} ")
        for treinos in treinosEncontrados:
            print(treinos.strip())
    else:
        print(f"Nenhum treino foi encontrado por {modo}")

#Adicionar metas

def adicionarMeta():
    metas = input("Anote uma meta de desempenho que você queira alcançar: ")

    with open(desempenhoTxt,"a",encoding="utf8") as metaFutura:
        metaFutura.write(metas + "; pendente")

    print("Parabéns, sua meta foi adicionada no sistema")

#Visualização das metas

def visualizarMeta():
    with open(desempenhoTxt, "r", encoding="utf8") as metaFutura:
        conteudo = metaFutura.readlines()

    if not conteudo:
        print("Nenhuma meta de desempenho foi registrada.")
        return

    print("Suas metas de desempenho:")
    for i, linha in enumerate(conteudo):
        try:
            objetivo, status = linha.strip().split(";")
            print(f"{i} - {objetivo.strip()} ({status.strip()})")
        except ValueError:
            print(f"{i} - [Formato inválido]: {linha.strip()}")

#Função para concluir a meta
def metaConcluida():
    visualizarMeta()
    indice = int(input("Digite o índice da meta que você concluiu: "))

    with open(desempenhoTxt, "r", encoding="utf8") as metaFutura:
        meta = metaFutura.readlines()

    if 0 <= indice < len(meta):
        metas, _ = meta[indice].strip().split(";")
        meta[indice] = f"{metas}; Concluída\n"

        with open(desempenhoTxt, "w", encoding="utf8") as metaFutura:
            metaFutura.writelines(meta)

        print("Parabéns! Meta marcada como concluída.")
    else:
        print("Índice inválido.")

#Escolha de treino aleatoriamente 
def escolhaTreino():
    with open(arquivo, "r", encoding="utf8") as dados:
        treinos = dados.readlines()
    
    if not treinos:
        print("Nenhum treino registrado ainda.")
        return
    
    treino_aleatorio = random.choice(treinos)
    tipo_treino = treino_aleatorio.split(";")[1].strip()
    
    print("\nTreino sugerido para hoje:", tipo_treino)

# visão usuário
while True:
    print("-------------------------------- ")
    print("---------- WOD TRACKER ---------")
    print("-------------------------------- ")

    print("A wod tracker permite que você possa adicionar/visualizar/editar/excluir registros do seu treino de CrossFit.")
    print("Digite 1, caso queira adicionar.")
    print("Digite 2, caso queira visualizar.")
    print("Digite 3, caso queira editar.")
    print("Digite 4, caso queira excluir.")
    print("Digite 5, caso queira filtrar por tipo ou movimento. ")
    print("Digite 6, caso queira adicionar metas de desempenho para o futuro. ")
    print("Digite 7, caso queira visualizar sua metas de desempenho ")
    print("Digite 8, caso queira marcar como concluída alguma meta")
    print("Digite 9, caso queira que selecionar um treino aleatório")
    print("Digite 10, caso queira sair do programa")
    escolha = int(input())

    if escolha == 1:
        novoTreino()
    elif escolha == 2:
        listarTreino()
    elif escolha == 3:
        editarTreino()
    elif escolha == 4:
        excluirTreino()
    elif escolha == 5:
        filtraTreino()
    elif escolha == 6:
        adicionarMeta()
    elif escolha == 7:
        visualizarMeta()
    elif escolha == 8:
        metaConcluida()
    elif escolha == 9:
        escolhaTreino()
    elif escolha == 10:
        break
    else:
        print("Opção inválida.")
