import simple_screen
import panel_screen
import customtkinter
import login_func
import conection
from tkinter import messagebox

def add_widgets_func(window):

    sql_register_street = f'SELECT DISTINCT street_name FROM register_user_{login_func.nick_name}'
    conection.mycursor.execute(sql_register_street)
    myresult_register_street = conection.mycursor.fetchall()

    text_street = customtkinter.CTkLabel(window, text="Rua:")
    type_street = [str(myresult_register_street[i][0]) for i in range(0, len(myresult_register_street))]
    street_option = customtkinter.CTkOptionMenu(window, values=type_street)

    input_quantity = customtkinter.CTkEntry(window, placeholder_text="Quantidade de pessoas:")


    text_street.pack(padx=10, pady=10)
    street_option.pack(padx=10, pady=10)
    input_quantity.pack(padx=10, pady=10)

def click_button_insert():
    print('insert')

def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def insert_multiple():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('INSERIR', 'DodgerBlue2', 'SteelBlue2', click_button_insert, 'insert'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Inserção Multipla', buttons_list, add_widgets_func)

if __name__ == '__main__':
    insert_multiple()
