import simple_screen
import panel_screen
import customtkinter
import conection
import insert_multple
from tkinter import *
from customtkinter import *
from tkinter import messagebox
import login_func
import delete_production


def add_widgets_func(window):

    sql_register_users = f'SELECT * FROM register_user_{login_func.nick_name}'
    conection.mycursor.execute(sql_register_users)
    myresult_register_users = conection.mycursor.fetchall()

    global family_option
    global input_date

    text_family = customtkinter.CTkLabel(window, text='Responsável Familiar:')
    type_family = [str(myresult_register_users[i][1]) for i in range(0, len(myresult_register_users))]
    family_option = customtkinter.CTkOptionMenu(window, values=type_family)

    input_date = customtkinter.CTkEntry(window, placeholder_text="Data:")

    text_family.pack(padx=10, pady=10)
    family_option.pack(padx=10, pady=10)
    input_date.pack(padx=10, pady=10)


def click_button_insert_family():

    name_family = family_option.get()
    date = input_date.get()

    # Use parameterized query: the column name must be a literal in SQL
    # here we assume the column that stores the family name is called `name`
    sql_register_user = f"SELECT quantity FROM register_user_{login_func.nick_name} WHERE name = %s"
    conection.mycursor.execute(sql_register_user, (name_family,))
    myresult_register_user = conection.mycursor.fetchone()

    # myresult_register_user will be a single row like (quantity,), or None
    if myresult_register_user:
        quantity = myresult_register_user[0]
    else:
        quantity = 0

    conection.mycursor.execute(
        f"INSERT INTO prod_{login_func.nick_name} (name, date, quantity) VALUES (%s, %s, %s)",
        (name_family, date, quantity)
    )
    conection.mydb.commit()

    family_option.set('')
    input_date.delete(0, 'end')
    
    
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")



def click_button_simple():
    simple_screen.window.destroy()

    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('INSERIR FAMÍLIA', 'DodgerBlue2', 'SteelBlue2', click_button_insert_family, 'f-insert'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return_2, 'return'))

    simple_screen.create_screen('500x300', 'Inserção Simples', buttons_list, add_widgets_func)

def click_button_multiple():
    simple_screen.window.destroy()
    insert_multple.insert_multiple()

def click_button_return_2():
    simple_screen.window.destroy()
    prod_list_screen()

def click_button_register():
    simple_screen.window.destroy()

    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('INSERÇÃO SIMPLES', 'DodgerBlue2', 'SteelBlue2', click_button_simple, 's-insert'))
    buttons_list.append(simple_screen.ArrayButton('INSERÇÃO MULTIPLA', 'DodgerBlue2', 'SteelBlue2', click_button_multiple, 'm-insert'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return_2, 'return'))

    simple_screen.create_screen('500x300', 'Inserção de Produção', buttons_list)

def click_button_update():
    print('update')

def click_button_delete():
    simple_screen.window.destroy()
    delete_production.delete_production()

def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def prod_list_screen():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('CADASTRAR', 'DodgerBlue2', 'SteelBlue2', click_button_register, 'r-user'))
    buttons_list.append(simple_screen.ArrayButton('ATUALIZAR', 'DodgerBlue2', 'SteelBlue2', click_button_update, 'u-user'))
    buttons_list.append(simple_screen.ArrayButton('EXCLUIR', 'DodgerBlue2', 'SteelBlue2', click_button_delete, 'd-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list)

if __name__ == '__main__':
    prod_list_screen()