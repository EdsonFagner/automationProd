import simple_screen
import panel_screen

def click_button_register():
    print('register')

def click_button_update():
    print('update')

def click_button_delete():
    print('delete')

def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def register_user_screen():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR', 'DodgerBlue2', 'SteelBlue2', click_button_register, 'r-user'))
    buttons_list.append(simple_screen.ArrayButton('ATUALIZAR', 'DodgerBlue2', 'SteelBlue2', click_button_update, 'u-user'))
    buttons_list.append(simple_screen.ArrayButton('EXCLUIR', 'DodgerBlue2', 'SteelBlue2', click_button_delete, 'd-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list)
    
if __name__ == '__main__':
    register_user_screen()

