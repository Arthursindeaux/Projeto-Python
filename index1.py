import os

arquivo = "Banco de Dados.txt"

#Função para adicionar um novo treino

def novoTreino():
        data = input("Em que dia foi feito seu treino: dia/mês/ano ")
        tipoTreino = input("O que você treinou ? (AMARAP/EMOM/FOR TIME) ")
        tempo = input("Quanto tempo durou o seu treino: (em minutos) ")
        movimentos = input("Quais movimentos tiveram no treino: ")

        with open(arquivo, "a",encoding="utf8") as dados:
            dados.write(f"{data}; {tipoTreino}; {tempo}; {movimentos}\n")
    
            print("O seu treino foi adicionado ! ")

#Função para visualizar um treino

def listarTreino():
     with open(arquivo, "r", encoding="utf8") as dados:
          conteudo = dados.readlines()
          if  conteudo == "":
            print("Você ainda não tem nenhum treino registrado ")
          else:
               print("Aqui está os treinos que você tem registrado: ")
               for i,linhas in enumerate(conteudo):
                print(f"{i} - {linhas.strip()}")
               
#Função para editar treino,Porém não estou conseguindo enumera-las do jeito certo.

def editarTreino():
    listarTreino()
    substituicao = int(input("Qual treino você quer editar ?"))
    with open(arquivo, "r", encoding="utf8") as dados:
        treinos = dados.readlines()
    
    if 0 <= substituicao < (len(treinos)):
         data = input("Substitua a data caso necessário: [dia/mês/ano]")
         tipoTreino =input("Substitua o tipo de treino caso necessário: ")
         tempo =input("Substitua o tempo do caso necessário: (em minutos)")
         movimentos = input("Substitua os movimentos caso necessário: ")
         treinos[substituicao] = (f"{data},{tipoTreino},{tempo},{movimentos}\n ")

         with open(arquivo, "w", encoding="utf8") as dados:
                dados.write(treinos)
         print("O seu treino foi atualizado! ")
    else:
        print("Indice inválido")

#Função para excluir o treino

while True:

    print("-------------------------------- ")
    print("---------- WOD TRACKER ---------")
    print("-------------------------------- ")

    print("A wod tracker permite que você possa adicionar/visualizar/editar/excluir registros do seu treino de CrossFit ")
    print("Digite 1, caso queira adicionar ")
    print("Digite 2, caso queira visualizar ")
    print("Digite 3, caso queira editar ")
    print("Digite 4, caso queira excluir ")
    escolha = int(input())

    if escolha == 1:
        novoTreino()

    if escolha == 2:
        listarTreino()
    
    if escolha == 3:
         editarTreino()

    if escolha ==4:
        excluirTreino()





