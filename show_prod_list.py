import simple_screen
import panel_screen
import customtkinter
import login_func
import conection
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

def add_widgets_func(window):
    print('show_prod_list')
    # Mostrar uma lista com todas as inserções na lista de produção do usuário logado na tabela prod_login_name
    sql_show_prod_list = f'SELECT * FROM prod_{login_func.nick_name}'
    conection.mycursor.execute(sql_show_prod_list)
    myresult_show_prod_list = conection.mycursor.fetchall()

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

    simple_screen.create_screen('500x400', 'Deletar Produção', buttons_list, add_widgets_func)


if __name__ == '__main__':
    show_prod_list()