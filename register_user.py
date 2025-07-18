import simple_screen
import register_user_screen
import pandas as pd
import customtkinter

def add_widgets_func(window):
    global input_name
    global input_quantity

    input_name = customtkinter.CTkEntry(window, placeholder_text='Responsável Familiar:')
    input_quantity = customtkinter.CTkEntry(window, placeholder_text='Qtd de Membros:')

    input_name.pack(padx=10, pady=10)
    input_quantity.pack(padx=10, pady=10)


def register():
    table_register = pd.read_excel('tables/table_register.xlsx', engine='openpyxl')
    index_table = len(table_register.loc[table_register['id']]+1)
    name_owner = input_name.get()
    quantity_members = input_quantity.get()


def click_button_return():
    simple_screen.window.destroy()
    register_user_screen.register_user_screen()

def register_user():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR', 'DodgerBlue2', 'SteelBlue2', register, 'r-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list, add_widgets_func)

if __name__ == '__main__':
    register_user()