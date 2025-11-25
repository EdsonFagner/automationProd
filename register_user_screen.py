import simple_screen
import panel_screen
import register_user
import delete_user

def click_button_register():
    simple_screen.window.destroy()
    register_user.register_user()

def click_button_delete():
    simple_screen.window.destroy()
    delete_user.delete_user()

def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def register_user_screen():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR', 'DodgerBlue2', 'SteelBlue2', click_button_register, 'r-user'))
    buttons_list.append(simple_screen.ArrayButton('EXCLUIR', 'DodgerBlue2', 'SteelBlue2', click_button_delete, 'd-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list)
    
if __name__ == '__main__':
    register_user_screen()

