import simple_screen
import conection
import login_func
import customtkinter
import list_prod
import mysql.connector
from tkinter import messagebox

def add_widgets_func(window):

    sql_date = f'SELECT DISTINCT date FROM prod_{login_func.nick_name}'

    try:
        conection.mycursor.execute(sql_date)
        myresult_date = conection.mycursor.fetchall()
    except mysql.connector.errors.OperationalError:
        # try to reconnect once and retry the query
        try:
            conection.reconnect()
            conection.mycursor.execute(sql_date)
            myresult_date = conection.mycursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco: {e}")
            myresult_date = []


    sql_name = f'SELECT DISTINCT name FROM prod_{login_func.nick_name}'

    try:
        conection.mycursor.execute(sql_name)
        myresult_name = conection.mycursor.fetchall()
    except mysql.connector.errors.OperationalError:
        # try to reconnect once and retry the query
        try:
            conection.reconnect()
            conection.mycursor.execute(sql_name)
            myresult_name = conection.mycursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco: {e}")
            myresult_name = []
    
    global date_option
    global name_option

    text_date = customtkinter.CTkLabel(window, text="Data:")
    type_date = [str(myresult_date[i][0]) for i in range(0, len(myresult_date))]
    type_date.insert(0, 'Selecione')
    date_option = customtkinter.CTkOptionMenu(window, values=type_date)


    text_name = customtkinter.CTkLabel(window, text="Nome:")
    type_name = [str(myresult_name[i][0]) for i in range(0, len(myresult_name))]
    type_name.insert(0, 'Selecione')
    name_option = customtkinter.CTkOptionMenu(window, values=type_name)
    

    text_date.pack(padx=10, pady=10)
    date_option.pack(padx=10, pady=10)
    text_name.pack(padx=10, pady=10)
    name_option.pack(padx=10, pady=10)
    


def click_button_delete():
    date_selected = date_option.get()
    name_selected = name_option.get()

    if(date_selected != 'Selecione'):
        sql_delete = f'DELETE FROM prod_{login_func.nick_name} WHERE date = "{date_selected}"'
        conection.mycursor.execute(sql_delete)
        conection.mydb.commit()
        messagebox.showinfo("Sucesso", "Produção deletada com sucesso!")

    elif(name_selected != 'Selecione'):
        sql_delete = f'DELETE FROM prod_{login_func.nick_name} WHERE name = "{name_selected}"'
        conection.mycursor.execute(sql_delete)
        conection.mydb.commit()
        messagebox.showinfo("Sucesso", "Produção deletada com sucesso!")
    
    else:
        messagebox.showerror("Erro", "Selecione uma data ou um nome.")

    
    date_option.set('Selecione')
    name_option.set('Selecione')


def click_button_return():
    simple_screen.window.destroy()
    list_prod.prod_list_screen()

def delete_production():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('DELETAR', 'red', 'red4', lambda: click_button_delete(), 'delete'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'DodgerBlue2', 'SteelBlue2', click_button_return, 'return'))

    simple_screen.create_screen('500x400', 'Deletar Produção', buttons_list, add_widgets_func)





if __name__ == '__main__':
    delete_production()