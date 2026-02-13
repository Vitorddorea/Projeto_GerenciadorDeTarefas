from time import sleep
# ==============================
# Funções do programa
# ==============================

def titulos(txt):
    """
    -> Padroniza os titúlos das funções
    
    :param txt: Título da Função 
    """

    print('=' * 35)
    print(txt.center(35))
    print('=' * 35)

def menu():
    """
    -> Menu visual do programa 

    """
    titulos('GERENCIADOR DE TAREFAS')
    print('1 - Criar Tarefa')
    print('2 - Verficar de Urgência')
    print('3 - Atualizar Tarefa')
    print('4 - Concluir Tarefa')
    print('5 - Excluir ')
    print('6 - Relatório')
    print('7 - Encerrar programa')
    print('=' * 35)


def tarefaExiste(gerenciador):
    if not gerenciador:
        print('Nenhuma tarefa cadastrada.')
        return None
     
    try:
        escolha = int(input('Digite o ID da tarefa: '))
        return escolha 
    except ValueError:
        print('\33[31mERRO! Digite um número.\33[m')
        return None


def gerarNovoId(gerenciador):
    """
    Gera um novo ID único para a tarefa.
    """
    if not gerenciador:
        return 1
    return max(tarefa['ID'] for tarefa in gerenciador) + 1


def criarTarefa(gerenciador):
    """
    -> Cria uma nova tarefa e adiciona ao gerenciador de tarefas
    :param gerenciador: lista que armazena todas tarefas
    """

    tarefa = {}
    
    titulos('CRIAR TAREFAS')
    
    tarefa['ID'] = gerarNovoId(gerenciador)   
    tarefa['Título'] = input('Título: ')
    tarefa['Prioridade'] = input('Prioridade [Urgente, Alta, Média ou Baixa]: ')
    tarefa['Status'] = input('Status [Pendente, Fazendo, Concluída]: ')
    tarefa['Origem'] = input('Origem da Tarefa [E-mail, Telefone, Chamado do Sistema]: ')
    
    gerenciador.append(tarefa)

    print('Adicionando Tarefa...')
    sleep(0.5)


def verificarUrgencia(gerenciador):
    titulos('VERIFICANDO URGENCIA')
    
    escolha = tarefaExiste(gerenciador)
    if escolha is None:
        return
    
    for tarefa in gerenciador:
        if tarefa['ID'] == escolha:
            print(tarefa['ID'], tarefa['Título'], tarefa['Status'])

            try:
                oque = int(input('O que quer fazer com essa tarefa? \n' 
                '1 - Atualizar Prioridade\n' 
                '2 - Concluir Tarefa\n' 
                '3 - Excluir'))
            except ValueError:
                print('\33[31mERRO! Digite um número.\33[m')
                return
            
            if oque == 1:
                print('Atualizar prioridade')
            elif oque == 2:
                print('Concluir tarefa')
            elif oque == 3:
                print('Excluir tarefa')
            else:
                print('Opção inválida')

            break
    else:
        print('Tarefa não encontrada.')


#def atualizarTarefa(gerenciador):

    
def relatorio(gerenciador):
    """
    -> Exibe um relatório com todas as tarefas cadastradas.
    """

    titulos('RELATÓRIO')

    if not gerenciador:
        print('Nenhuma tarefa cadastrada.')
    else:
        for tarefa in gerenciador:
            
            print(f'ID: {tarefa["ID"]} | Título: {tarefa["Título"]} | Prioridade: {tarefa["Prioridade"]} | Status: {tarefa["Status"]} | Origem: {tarefa["Origem"]}')


# ==============================
# Lista de Tarefas
# ==============================

gerenciador = []

# ==============================
# Loop principal do programa
# ==============================

while True:
    menu()
    
    while True:
        try:
            opcao = int(input('O que gostaria de fazer?: '))
        except ValueError: 
            print('\33[31mERRO! Digite um número.\33[m')
        else:
            if 1 <= opcao <=7:
                break
            else:
                print('\33[31mERRO! Digite uma opção valida.\33[m')

    if opcao == 1:
        criarTarefa(gerenciador)
    elif opcao == 2:
        verificarUrgencia(gerenciador)
    elif opcao == 3:
        atualizarTarefa(gerenciador)
    elif opcao == 4:
        print('Concluindo Tarefa')
    elif opcao == 5:
        print('Excluindo Tarefa')
    elif opcao == 6:
        relatorio(gerenciador)
    elif opcao == 7:
        print('Encerrando programa...')
        sleep(0.5)
        break
    



