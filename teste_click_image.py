import time
import navigator_func
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import simple_screen
import os
import customtkinter
from tkinter import messagebox

def minimize_window(window):
    window.iconify()

def restore_window(window):
    window.deiconify()

def add_widgets_screen(window):
    global input_text_element
    input_text_element = customtkinter.CTkEntry(window, placeholder_text='Elemento:') 
    input_text_element.pack(padx=10, pady=10)

def click_button_navigator():
    navigator_func.navigator_settings()
    time.sleep(3)


def click_button_click_element():
    input_element = input_text_element.get()
    time.sleep(3)
    minimize_window(simple_screen.window)
    try:
        button_notification_xpath = input_element
        button_notification = WebDriverWait(navigator_func.navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, button_notification_xpath))
        )
        print('clicou')
        action = ActionChains(navigator_func.navegador)
        action.click(button_notification).perform()
    except Exception as e:
        restore_window(simple_screen.window)
        messagebox.showerror("Erro", f"Erro ao clicar no elemento: {e}")
        pass

def click_button_exit():
    navigator_func.navegador.quit()
    os._exit(0)


def main():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('ABRIR NAVEGADOR', 'DodgerBlue2', 'SteelBlue2', click_button_navigator, 'Navegador'))
    buttons_list.append(simple_screen.ArrayButton('CLICAR ELEMENTO', 'DodgerBlue2', 'SteelBlue2', click_button_click_element, 'Click'))
    buttons_list.append(simple_screen.ArrayButton('Sair', 'red', 'red4', lambda: click_button_exit(), 'Sair'))

    simple_screen.create_screen('400x400', 'Painel de Controle', buttons_list, add_widgets_screen)
    


if __name__ == '__main__':
    main()