import simple_screen
import panel_screen
import customtkinter
import login_func
import conection
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_widgets_func(window):
    print('show_prod_list')
    query = ''
    params = None

    if not conection.pool_conexoes:
        messagebox.showerror("Erro", "Erro ao acessar o banco de dados, não existe pool de conexões.")
        return None
    
    try:
        query = f'SELECT * FROM prod_{login_func.nick_name}'
        with conection.pool_conexoes.get_connection() as connection:
            print('Conectado ao banco de dados')
            with conection.mydb.cursor() as mycursor:
                mycursor.execute(query, params)
                if query.strip().upper().startswith('SELECT'):
                    myresult_show_prod_list = mycursor.fetchall()
                else:
                    messagebox.showinfo("Erro", "Não foi possivel executar a query.")

    except conection.mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {err}")
        return None
    # Mostrar uma lista com todas as inserções na lista de produção do usuário logado na tabela prod_login_name
    #sql_show_prod_list = f'SELECT * FROM prod_{login_func.nick_name}'
    #conection.mycursor.execute(sql_show_prod_list)
    #myresult_show_prod_list = conection.mycursor.fetchall()

    # Se não houver registros, mostrar mensagem e sair
    if not myresult_show_prod_list:
        customtkinter.CTkLabel(window, text='Nenhum registro encontrado.').pack(padx=10, pady=10)
        return

    # Container para a tabela
    table_frame = tk.Frame(window)
    # Tenta usar a mesma cor de fundo da janela para integrar com o tema
    try:
        bg_color = window.cget('bg')
    except Exception:
        bg_color = '#2b2b2b'
    table_frame.configure(bg=bg_color)
    table_frame.pack(fill='both', expand=True, padx=10, pady=10)

    # Estiliza a Treeview para ter fundo igual à janela e texto branco
    style = ttk.Style()
    try:
        style.theme_use('clam')
    except Exception:
        pass
    style.configure('Treeview', background=bg_color, fieldbackground=bg_color, foreground='white')
    style.configure('Treeview.Heading', background=bg_color, foreground='white')
    style.map('Treeview', background=[('selected', '#4a6984')], foreground=[('selected', 'white')])

    columns = ('name', 'date', 'quantity')
    tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=10)

    tree.heading('name', text='Nome')
    tree.heading('date', text='Data')
    tree.heading('quantity', text='Quantidade')

    tree.column('name', width=220, anchor='w')
    tree.column('date', width=120, anchor='center')
    tree.column('quantity', width=120, anchor='center')

    vsb = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')

    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)

    # Inserir dados na tabela (assume-se que a linha seja (id, name, date, quantity))
    for row in myresult_show_prod_list:
        tree.insert('', 'end', values=(row[1], row[2], row[3]))


def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def show_prod_list():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('VOLTAR',  'red', 'red4',  click_button_return, 'return'))

    simple_screen.create_screen('500x400', 'Exibir Lista', buttons_list, add_widgets_func)


if __name__ == '__main__':
    show_prod_list()