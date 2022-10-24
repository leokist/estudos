"""
UNICESUMAR
ALUNO: LEONARDO HENRIQUE MARIN KIST
MAPA DA DISCIPLINA - FUNDAMENTOS DE PROGRAMAÇÃO COM PYTHON ESP
PROGRAMA AGENDA
"""

# Exibe tela inicial com todas as opções do programa
def inicio():
    print(85*"#")
    print("LISTA DE CONTATOS - MENU".center(85, " "))
    print(85*"#")
    print("1 - Cadastrar Pessoa na Agenda")
    print("2 - Alterar Dados da Pessoa")
    print("3 - Listar Agenda")
    print("4 - Procurar Pessoa na Agenda")
    print("5 - Excluir Pessoa da Agenda")
    print("6 - Sair do Programa")
    print(85*"-")

    # Definição da variável em escopo global
    global opção
    opção=int(input(">>> Digite o número de uma opção existente: "))
    # verifica se foi digitada uma opção válida
    if opção > 6 or opção < 1:
        while  opção > 6 or opção < 1:
            print("Opção inexistente, digite uma opção válida!")
            opção=int(input(">>> Digite o número de uma opção existente: "))

    # encerrar o programa
    if opção == 6:
        print(85*"#")
        print("O programa será encerrado!!")
        print(85*"#")

# cria a agenda
global agenda
agenda = []


# função para inserir um novo cadastro
# cada palavra terá a primeira letra de cada palavra em caixa alta e o restante minúsculo
def novo_cadastro():
    nome=str(input(">>> Digite o nome: ").title())
    telefone=str(input(">>> Digite o telefone: ").title())
    cidade=str(input(">>> Digite a cidade: ").title())
    estado=str(input(">>> Digite o estado: ").title())
    status=str(input(">>> Digite p para pessoal ou c para comercial: ").title())
    agenda.append([nome, telefone, cidade, estado, status])


# função para alterar o cadastro
def alterar_cadastro():
    buscar_nome=str(input(">>> Digite o nome do contato que deseja alterar: ").title())

    # exibe todos os contatos encontrados
    print(85*"-")
    print("OS CONTATOS ENCONTRADOS FORAM:".center(85," "))
    cabecalho()
    contador = 0
    for a in agenda:
        if buscar_nome in a:
            i = agenda.index(a)
            print(contador,
                agenda[i][0].center(18," "),
                agenda[i][1].center(15," "),
                agenda[i][2].center(20," "),
                agenda[i][3].center(19," "),
                agenda[i][4].center(6," "))
            contador += 1
    print(f"Encontrado(s) {contador} contato(s)")

    if contador == 0:
        print("Nada encontrado para ser alterado!")
    elif contador != 0:
        # solicita qual item deverá ser alterado
        item=int(input(">>> Digite o número do item que deseja alterar: "))
        # se digitado número inválido apresenta erro e repete o processo
        while item > contador-1 or item < 0:
            print("Digite uma opção válida!")
            item=int(input(">>> Digite o número do item que deseja alterar: "))
        # solicita para digitar os campos para serem alterados
        print("Caso algum campo fique em branco o mesmo não será alterado!!")
        nome=str(input(">>> Altere o nome: ").title())
        telefone=str(input(">>> Altere o telefone: ").title())
        cidade=str(input(">>> Altere a cidade: ").title())
        estado=str(input(">>> Altere o estado: ").title())
        status=str(input(">>> Altere status: p para pessoal ou c para comercial: ").title())
        # somente irá alterar caso não tenha ficado em branco
        if nome!="":
            agenda[item][0]=nome
        if telefone!="":
            agenda[item][1]=telefone
        if cidade!="":
            agenda[item][2]=cidade
        if estado!="":
            agenda[item][3]=estado
        if status!="":
            agenda[item][4]=status
        print("O item foi alterado!")


# função para invocar o cabeçalho da tabela
def cabecalho():
    print("NOME".center(20," "),
        "TELEFONE".center(15," "),
        "CIDADE".center(20," "),
        "ESTADO".center(19," "),
        "STATUS".center(6," "))


# função para procurar uma pessoa na agenda
def procurar_cadastro():
    buscar_nome=str(input(">>> Digite o nome desejado: ").title())
    # imprime o cabeçalho da agenda
    print(85*"-")
    print("OS CONTATOS ENCONTRADOS FORAM:".center(85," "))
    cabecalho()
    # pesquisa o nome dentro de cada sub-lista da agenda
    contador = 0
    for a in agenda:
        if buscar_nome in a:
            i = agenda.index(a)
            print(agenda[i][0].center(20," "),
                agenda[i][1].center(15," "),
                agenda[i][2].center(20," "),
                agenda[i][3].center(19," "),
                agenda[i][4].center(6," "))
            contador += 1
    if contador == 0:
        print("Nenhum contato foi encontrado")
    elif contador > 0:
        print(f"Somente {contador} contato(s) encontrado(s)")


# função para deletar o cadastro
def deletar_cadastro():
    # solicita o nome que deseja deletar
    buscar_nome=str(input(">>> Pesquise o nome que deseja deletar da agenda: ").title())

    # exibe todos os contatos encontrados
    print(85*"-")
    print("OS CONTATOS ENCONTRADOS FORAM:".center(85," "))
    cabecalho()
    contador = 0
    for a in agenda:
        if buscar_nome in a:
            i = agenda.index(a)
            print(contador,
                agenda[i][0].center(18," "),
                agenda[i][1].center(15," "),
                agenda[i][2].center(20," "),
                agenda[i][3].center(19," "),
                agenda[i][4].center(6," "))
            contador += 1
    print(f"Encontrado(s) {contador} contato(s)")

    if contador == 0:
        print("Nada encontrado para ser deletado!")
    elif contador != 0:
        # solicita qual item deverá ser excluído
        item=int(input(">>> Digite o número do item que deseja deletar: "))
        # se digitado número inválido apresenta erro e repete o processo
        while item > contador-1 or item < 0:
            print("Digite uma opção válida!")
            item=int(input(">>> Digite o número do item que deseja deletar: "))
        # exclui o item da agenda
        agenda.pop(item)
        print("O item foi deletado!")


# função que irá listar o conteúdo da agenda
def listar_agenda():
    if agenda == []:
        # imprime mensagem caso a angeda esteja vazia
        print(85*"-")
        print("A AGENDA ESTÁ VAZIA".center(85," "))
    else:
        # imprime o cabeçalho da agenda
        print(85*"-")
        print("OS CONTATOS DA SUA LISTA SÃO:".center(85," "))
        cabecalho()
        # imprime o contúdo da agenda
        i=0
        for contato in agenda:
            print(agenda[i][0].center(20," "),
                agenda[i][1].center(15," "),
                agenda[i][2].center(20," "),
                agenda[i][3].center(19," "),
                agenda[i][4].center(6," "))
            i+=1


# função para somente continuar o programa após apertar ENTER
def continuar():
    print(85*"-")
    continuar=(input(">>> Aperte a tecla ENTER para continuar: "))


"""inicia a execução do programa"""
inicio()

# executa o programa enquanto a opção selecionada for entre 5 e 1
while opção <= 5 and opção >= 1:
    if opção == 1:
        novo_cadastro()
        continuar()
        inicio()
    elif opção == 2:
        alterar_cadastro()
        continuar()
        inicio()
    elif opção == 3:
        listar_agenda()
        continuar()
        inicio()
    elif opção == 4:
        procurar_cadastro(),
        continuar()
        inicio()
    elif opção == 5:
        deletar_cadastro()
        continuar()
        inicio()
