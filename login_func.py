import conection
import time
import customtkinter
from passlib.hash import bcrypt

#Declaração de variáveis
success_login = False
nick_name = None
#Declaração de variáveis mysql
sql = 'SELECT * FROM access_login'
conection.mycursor.execute(sql)
myresult = conection.mycursor.fetchall()

#Função acionada ao clicar no botão
def Click ():
    global success_login
    global nick_name
    up_to = len(myresult)
    count_invalid = 0
    for x in range(0, up_to):
        if(bcrypt.verify(user.get(), myresult[x][1])==True and bcrypt.verify(password.get(), myresult[x][2])==True):
            print('Login Success')
            success_login = True
            nick_name = myresult[x][3]
            time.sleep(1)
            window.destroy()
        else:
            count_invalid += 1
        
    if(count_invalid == len(myresult)):
        print('Login Fail')
        user._entry.delete(0, 'end')
        password._entry.delete(0, 'end')


#Configurações da tela do tkinter
def login():
    global window
    global text
    global user
    global password
    global button

    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')

    window = customtkinter.CTk()
    window.geometry('500x300')

    text = customtkinter.CTkLabel(window, text='Sistema de Login')

    user = customtkinter.CTkEntry(window, placeholder_text='Login:')

    password = customtkinter.CTkEntry(window, placeholder_text='Senha:', show='*')

    button = customtkinter.CTkButton(window, text='Login', command=Click)

    text.pack(padx=10, pady=10)
    user.pack(padx=10, pady=10)
    password.pack(padx=10, pady=10)
    button.pack(padx=10, pady=10)

    window.mainloop()


if __name__ == '__main__':
    login()