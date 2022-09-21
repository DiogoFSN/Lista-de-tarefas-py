
def mostra_lista(lista_de_tarefas):
    print()
    print('Tarefas: ')
    for i in lista_de_tarefas:
        print(f'- {i}')
    print()

def refazer(lista_de_tarefas, lista_refeita):
    if not lista_refeita:
        print()
        print('Nada a refazer.')
        print()
        return

    refaz = lista_refeita.pop()
    lista_de_tarefas.append(refaz)

def desfazer(lista_de_tarefas, lista_refeita):
    if not lista_de_tarefas:
        print()
        print('Nada a desfazer.')
        print()
        return

    desfaz = lista_de_tarefas.pop()
    lista_refeita.append(desfaz)

def add_list(operacao, lista_de_tarefas):
    lista_de_tarefas.append(operacao)

if __name__ == '__main__':
    lista_de_tarefas =  []
    lista_refeita = []

    while True:
        operacao = input(f'''Digite uma tarefa ou \n[0] para mostrar sua lista de tarefas, \n[1] para desfazer uma tarefa, \n[2] para refazer a ultima tarefa, \n[-1] para sair:\n ''')

        if operacao == '0':
            mostra_lista(lista_de_tarefas)
            continue
        elif operacao == '1':
            desfazer(lista_de_tarefas, lista_refeita)
            continue
        elif operacao == '2':
            refazer(lista_de_tarefas, lista_refeita)
            continue
        elif operacao == '-1':
            break
        
        add_list(operacao, lista_de_tarefas)

        

