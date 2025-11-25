import simple_screen
import customtkinter
import register_user_screen
import conection
import login_func
from tkinter import messagebox

#Declaração de variáveis mysql
sqlAcess = 'SELECT * FROM access_login'
conection.mycursor.execute(sqlAcess)
myresultAcess = conection.mycursor.fetchall()
table_nickname = None



def add_widgets_func(window):
    global input_name
    global input_street

    input_name = customtkinter.CTkEntry(window, placeholder_text='Responsável Familiar:')
    input_street = customtkinter.CTkEntry(window, placeholder_text='Rua:')

    input_name.pack(padx=10, pady=10)
    input_street.pack(padx=10, pady=10)

def delete():
    countIncorrect = 0

    for x in range(0, len(myresultAcess)):
        print(f'Chegou{x}')
        nickName = myresultAcess[x][3]
        print(nickName)
        if nickName == login_func.nick_name:
            print(f'Chegou no if nickname')
            name_owner = input_name.get()
            street_name = input_street.get()
            table_nickname = f'register_user_{nickName}'
            mycursor = conection.mycursor
            mycursor.execute(f'SELECT * FROM {table_nickname}')
            result = mycursor.fetchall()
            if result:
                print(f'Chegou no if result')
                countIncorrect = 0
                for y in range(0, len(result)):
                    print(f'Chegou no for result {y}')
                    if result[y][1] == name_owner and result[y][3] == street_name:
                        conection.mycursor.execute(f'DELETE FROM {table_nickname} WHERE name = %s AND street_name = %s', (name_owner, street_name))
                        conection.mydb.commit()
                        messagebox.showinfo("Sucesso", "Cadastro deletado com sucesso!")
                        input_name.delete(0, 'end')
                        input_street.delete(0, 'end')
                        return
                    else:
                        countIncorrect += 1
                
                if countIncorrect == len(result):
                    messagebox.showerror("Erro", "Cadastro nao encontrado!")
                    return
            else:
                messagebox.showerror("Erro", "Nenhum cadastro encontrado!")
                return
        else:
            countIncorrect += 1

    if countIncorrect == len(myresultAcess):
        messagebox.showerror("Erro", "Usuario sem permissão!")
def click_button_return():
    simple_screen.window.destroy()
    register_user_screen.register_user_screen()

def delete_user():
    buttons_list = []
    buttons_list.append(simple_screen.ArrayButton('DELETAR', 'DodgerBlue2', 'SteelBlue2', delete, 'd-user'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x300', 'Cadastro de Usuários', buttons_list, add_widgets_func)

if __name__ == '__main__':
    delete_user()
    