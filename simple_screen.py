import customtkinter

class ArrayButton:
    def __init__(self, textButton, fgColor, hvColor, commandFunction, nameButton):
        self.textButton = textButton
        self.fgColor = fgColor
        self.hvColor = hvColor
        self.commandFunction = commandFunction
        self.nameButton = nameButton

def create_button(window, textButton, fgColor, hvColor, commandFunction, nameButton):
    btn = customtkinter.CTkButton(window, text=textButton, fg_color=fgColor, hover_color=hvColor, command=commandFunction)
    return btn

def show_button(window, arrayButtons):
    buttons = []
    for btn_obj in arrayButtons:
        btn = create_button(window, btn_obj.textButton, btn_obj.fgColor, btn_obj.hvColor, btn_obj.commandFunction, btn_obj.nameButton)
        btn.pack(padx=10, pady=10)
        buttons.append(btn)
    return buttons

def close_window():
    window.destroy()

def create_screen(size, title, arrayButtons, add_widgets_func=None):
    global window
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    window = customtkinter.CTk()
    window.geometry(size)
    window.title(f'ProdProject - {title}')
    window.iconbitmap('')
    text = customtkinter.CTkLabel(window, text=f'{title}: ').pack(padx=10, pady=10)
    # Adiciona widgets extras se função for passada
    if add_widgets_func:
        add_widgets_func(window)
    show_button(window, arrayButtons)
    window.mainloop()

if __name__ == '__main__':
    create_screen()