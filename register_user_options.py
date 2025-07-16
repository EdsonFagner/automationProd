import simple_screen
import register_user

def register_manual():
    simple_screen.window.destroy()

def register_auto():
    simple_screen.window.destroy()
    print('register_auto')

def click_button_return():
    simple_screen.window.destroy()
    register_user.register_user_screen()

def register_user_options():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR MANUALMENTE', 'DodgerBlue2', 'SteelBlue2', register_manual, 'r-user'))
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR AUTOMATICAMENTE', 'DodgerBlue2', 'SteelBlue2', register_auto, 'a-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list)