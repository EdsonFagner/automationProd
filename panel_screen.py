import simple_screen
import register_user_screen
import list_prod
import show_prod_list
import exec_prod


def register_users():
    simple_screen.window.destroy()
    register_user_screen.register_user_screen()

def register_prodution_list():
    simple_screen.window.destroy()
    list_prod.prod_list_screen()

def prod_list():
    simple_screen.window.destroy()
    show_prod_list.show_prod_list()

def send_prodution():
    simple_screen.window.destroy()
    exec_prod.exec_prodution()

def close_window():
    simple_screen.window.destroy()


def panel_screen():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRO DE USUÁRIOS', 'DodgerBlue2', 'SteelBlue2', register_users, 'c-users'))
    buttons_list.append(simple_screen.ArrayButton('CADASTRO DE LISTA DE PRODUÇÃO', 'DodgerBlue2', 'SteelBlue2', register_prodution_list, 'c-prodution'))
    buttons_list.append(simple_screen.ArrayButton('EXIBIR LISTAS', 'DodgerBlue2', 'SteelBlue2', prod_list, 'show-prodution'))
    buttons_list.append(simple_screen.ArrayButton('EVIAR PRODUÇÃO', 'DodgerBlue2', 'SteelBlue2', send_prodution, 'send-prodution'))
    buttons_list.append(simple_screen.ArrayButton('SAIR', 'red', 'red4', close_window, 'exit'))

    simple_screen.create_screen('500x300', 'Painel de Controle', buttons_list)

if __name__ == '__main__':
    panel_screen()