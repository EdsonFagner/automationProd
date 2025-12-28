import simple_screen
import list_prod
import customtkinter
import login_func
import conection
import mysql.connector
from tkinter import messagebox
import random

def add_widgets_func(window):

    sql_register_street = f'SELECT DISTINCT street_name FROM register_user_{login_func.nick_name}'
    # execute with basic retry in case the connection was lost
    try:
        conection.mycursor.execute(sql_register_street)
        myresult_register_street = conection.mycursor.fetchall()
    except mysql.connector.errors.OperationalError:
        # try to reconnect once and retry the query
        try:
            conection.reconnect()
            conection.mycursor.execute(sql_register_street)
            myresult_register_street = conection.mycursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao acessar o banco: {e}")
            myresult_register_street = []

    global street_option
    global input_quantity
    global input_date

    text_street = customtkinter.CTkLabel(window, text="Rua:")
    type_street = [str(myresult_register_street[i][0]) for i in range(0, len(myresult_register_street))]
    street_option = customtkinter.CTkOptionMenu(window, values=type_street)

    input_quantity = customtkinter.CTkEntry(window, placeholder_text="Quantidade de pessoas:")

    input_date = customtkinter.CTkEntry(window, placeholder_text="Data:")


    text_street.pack(padx=10, pady=10)
    street_option.pack(padx=10, pady=10)
    input_quantity.pack(padx=10, pady=10)
    input_date.pack(padx=10, pady=10)

def click_button_insert(): 
    street_name = street_option.get()
    quantity = input_quantity.get()
    date = input_date.get()
    quantity_members_family = 0
    quantity_members = 0

    #Pegar usuários aleatóriamente da rua em questão até formar a quantidade exata ou maior de pessoas e inserir no banco de dados
    sql_register_users = f'SELECT * FROM register_user_{login_func.nick_name} WHERE street_name = "{street_name}"'
    conection.mycursor.execute(sql_register_users)
    myresult_register_users = conection.mycursor.fetchall()
    users = [str(myresult_register_users[i][1]) for i in range(0, len(myresult_register_users))]
    random.shuffle(users)

    #Loop para pegar os usuários aleatóriamente da rua em questão até formar a quantidade exata ou maior de pessoas e inserir no banco de dados
    for i in range(quantity_members_family, int(quantity)):
       #If para interromper o for se a quantidade de pessoas for maior que a quantidade de pessoas desejada
        if quantity_members_family >= int(quantity):
            break
        
        #Pegando a quantidade de membros da família do usuário
        sql_quantity_users = f'SELECT quantity FROM register_user_{login_func.nick_name} WHERE name = "{users[i]}"'
        conection.mycursor.execute(sql_quantity_users)
        myresult_quantity_users = conection.mycursor.fetchone()

        #Incrementando a quantidade de usuários na contagem do looping
        quantity_members_family += myresult_quantity_users[0]

        #Pegando o nome do usuário e a quantidade de pessoas dele
        name_family = users[i]
        quantity_members = myresult_quantity_users[0]


        #Inserindo os dados no banco
        conection.mycursor.execute(
            f"INSERT INTO prod_{login_func.nick_name} (name, date, quantity) VALUES (%s, %s, %s)",
            (name_family, date, quantity_members)
        )
        conection.mydb.commit()

    street_option.set('')
    input_quantity.delete(0, 'end')
    input_date.delete(0, 'end')
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    

def click_button_return():
    simple_screen.window.destroy()
    list_prod.prod_list_screen()

def insert_multiple():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('INSERIR', 'DodgerBlue2', 'SteelBlue2', lambda: click_button_insert(), 'insert'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR', 'red', 'red4', click_button_return, 'return'))

    simple_screen.create_screen('500x400', 'Inserção Multipla', buttons_list, add_widgets_func)

if __name__ == '__main__':
    insert_multiple()
