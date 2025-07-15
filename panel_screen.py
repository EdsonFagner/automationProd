import simple_screen
import register_user
import list_prod

def register_users():
    simple_screen.window.destroy()
    register_user.register_user_screen()

def register_prodution_list():
    simple_screen.window.destroy()
    list_prod.prod_list_screen()

def show_prod_list():
    print('prodution')

def close_window():
    simple_screen.window.destroy()


def panel_screen():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRO DE USUÁRIOS', 'DodgerBlue2', 'SteelBlue2', register_users, 'c-users'))
    buttons_list.append(simple_screen.ArrayButton('CADASTRO DE LISTA DE PRODUÇÃO', 'DodgerBlue2', 'SteelBlue2', register_prodution_list, 'c-prodution'))
    buttons_list.append(simple_screen.ArrayButton('EXIBIR LISTAS', 'DodgerBlue2', 'SteelBlue2', show_prod_list, 'show-prodution'))
    buttons_list.append(simple_screen.ArrayButton('SAIR', 'red', 'red4', close_window, 'exit'))

    simple_screen.create_screen('500x300', 'Painel de Controle', buttons_list)

if __name__ == '__main__':
    panel_screen()