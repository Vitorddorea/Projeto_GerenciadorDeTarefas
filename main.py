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
    print('4 - Excluir ')
    print('5 - Relatório')
    print('6 - Encerrar programa')
    print('=' * 35)

def lerInt(msg):
    """
    -> Retorna um número inteiro válido

    :param msg: mensagem para o input
    """
    
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('\033[31mDigite um valor válido! \033[m')


def tarefaExiste(gerenciador):
    if not gerenciador:
        print('Nenhuma tarefa cadastrada.')
        return None

    escolha = lerInt('Digite o ID da tarefa: ')

    for tarefa in gerenciador:
        if tarefa['ID'] == escolha:
            return tarefa

    print('Tarefa não encontrada.')
    return None


def gerarNovoId(gerenciador):
    """
    Gera um novo ID único para a tarefa.
    """
    if not gerenciador:
        return 1
    return max(tarefa['ID'] for tarefa in gerenciador) + 1

def opcoes(txt = '', limite = 4):
    """
    Confere se é uma opçao válida
    """
    while True:
        opcao = lerInt(txt)
        if 1 <= opcao <= limite:
            return opcao
        else:
            print('\033[31mDigite uma opção válida! \033[m')    


def retPrioridade(txt):
    """
    Retona a prioridade
    """
    opcao = opcoes(txt, 4)

    if opcao == 1:
        return 'Urgente'
    elif opcao == 2:
        return 'Alta'
    elif opcao == 3:
        return 'Média'
    elif opcao == 4: 
        return 'Baixa'
    

def retStatus(txt):
    """
    Retorna o Status
    """
    
    opcao = opcoes(txt, 3)

    if opcao == 1:
        return 'Pendente'
    elif opcao == 2:
        return 'Fazendo'
    elif opcao == 3:
        return 'Concluída'
    
def retOrigem(txt):
    """
    Retorna a Origem
    """
    opcao = opcoes(txt, 3)

    if opcao == 1:
        return 'E-mail'
    elif opcao == 2:
        return 'Telefone'
    elif opcao == 3:
        return 'Chamado do Sistema'


def criarTarefa(gerenciador):
    """
    -> Cria uma nova tarefa e adiciona ao gerenciador de tarefas
    :param gerenciador: lista que armazena todas tarefas
    """

    tarefa = {}
    
    titulos('CRIAR TAREFAS')
    
    tarefa['ID'] = gerarNovoId(gerenciador)   
    tarefa['Título'] = input('Título: ')
    tarefa['Prioridade'] = retPrioridade('Prioridade [1 - Urgente, 2 - Alta, 3 - Média ou 4 - Baixa]: ')
    tarefa['Status'] = retStatus('Status [1 - Pendente, 2 - Fazendo, 3 - Concluída]: ')
    tarefa['Origem'] = retOrigem('Origem da Tarefa [1 - E-mail, 2 - Telefone, 3 - Chamado do Sistema]: ')
    
    gerenciador.append(tarefa)

    print('Adicionando Tarefa...')
    sleep(0.5)

def relatorio(gerenciador):
    """
    -> Exibe um relatório com todas as tarefas cadastradas.
    """

    titulos('RELATÓRIO')

    if not gerenciador:
        print('Nenhuma tarefa cadastrada.')
    else:
        for tarefa in gerenciador:
            print('-' * 35)
            print(f'ID: {tarefa["ID"]} | Título: {tarefa["Título"]} | Prioridade: {tarefa["Prioridade"]} | Status: {tarefa["Status"]} | Origem: {tarefa["Origem"]}')


def verificarUrgencia(gerenciador):

    titulos('TAREFAS URGENTES')

    encontrou = False

    for tarefa in gerenciador:
        if tarefa['Prioridade'] == 'Urgente' and tarefa['Status'] != 'Concluída':
            print(f'{tarefa["ID"]} - {tarefa["Título"]}')
            encontrou = True

    if not encontrou:
        print('Nenhuma tarefa urgente.')

def atualizarTarefa(gerenciador):
    """
    Atualiza uma tarefa 
    """

    relatorio(gerenciador)

    titulos('ATUALIZAR TAREFA')

    opcao = lerInt('Qual tarefa voce quer atualizar? ID: ')

    encontrado = False

    for tarefa in gerenciador:
        if tarefa['ID'] == opcao:
            oque = opcoes('O que você quer atualizar? 1 - Prioridade, 2 - Status, 3 - Origem : ', 3)
            
            if oque == 1:
                tarefa['Prioridade'] = retPrioridade('Prioridade [1 - Urgente, 2 - Alta, 3 - Média ou 4 - Baixa]: ')
            elif oque == 2:
                tarefa['Status'] = retStatus('Status [1 - Pendente, 2 - Fazendo, 3 - Concluída]: ')
            elif oque == 3:
                tarefa['Origem'] = retOrigem('Origem da Tarefa [1 - E-mail, 2 - Telefone, 3 - Chamado do Sistema]: ')
            encontrado = True
            break

    if encontrado:
        print(f'Tarefa do ID {opcao} atualizada!')
    else:
        print('Tarefa não encontrada.')

def deletarTarefa(gerenciador):
    """
    Deleta uma tarefa
    """
    
    relatorio(gerenciador)

    titulos('DELETAR TAREFA')

    opcao = lerInt('Qual tarefa voce quer deletar? ID: ')

    encontrado = False

    for tarefa in gerenciador:
        if tarefa['ID'] == opcao:
            gerenciador.remove(tarefa)
            encontrado = True
            break
    
    if encontrado:
        print(f'Tarefa do ID {opcao} deletada!')
    else:
        print('Tarefa não encontrada.')


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
        opcao = lerInt('O que gostaria de fazer?: ')
    
        if 1 <= opcao <= 6:
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
        deletarTarefa(gerenciador)
    elif opcao == 5:
        relatorio(gerenciador)
    elif opcao == 6:
        print('Encerrando programa...')
        sleep(0.5)
        break
    
