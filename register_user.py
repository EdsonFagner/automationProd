import simple_screen
import register_user_screen
import customtkinter
import conection
import login_func
from tkinter import messagebox

#Declaração de variáveis mysql
sqlAcess = 'SELECT * FROM access_login'
myresultAcess = conection.execute_query(sqlAcess, params=None)
table_nickname = None
countIncorrect = 0

sqlUsers = 'SELECT * FROM users'

def add_widgets_func(window):
    global input_name
    global input_quantity
    global input_street

    input_name = customtkinter.CTkEntry(window, placeholder_text='Responsável Familiar:')
    input_quantity = customtkinter.CTkEntry(window, placeholder_text='Qtd de Membros:')
    input_street = customtkinter.CTkEntry(window, placeholder_text='Rua:')

    input_name.pack(padx=10, pady=10)
    input_quantity.pack(padx=10, pady=10)
    input_street.pack(padx=10, pady=10)


def register():
    global countIncorrect
    
    for x in range(0, len(myresultAcess)):
        nickName = myresultAcess[x][3]
        if nickName == login_func.nick_name:
            name_owner = input_name.get()
            quantity_members = input_quantity.get()
            street_name = input_street.get()
            table_nickname = f'register_user_{nickName}'

            query = f'INSERT INTO {table_nickname} (name, quantity, street_name) VALUES (%s, %s, %s)'
            params = (str(name_owner), int(quantity_members), str(street_name))
            resultado = conection.execute_query(query, params, fetch=False)
            
            # Verificar se o insert foi bem-sucedido
            if resultado and resultado > 0:
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao inserir registro no banco de dados!")
                return
            
            input_name.delete(0, 'end')
            input_quantity.delete(0, 'end')
            input_street.delete(0, 'end')
            return
        else: 
            countIncorrect += 1

    if countIncorrect == len(myresultAcess):
        messagebox.showerror("Erro", "Usuario sem permissão!")


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