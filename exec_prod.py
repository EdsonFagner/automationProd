import simple_screen
import panel_screen
import func_exec_prod
import tk_async_execute as tk_async
import keyboard

class SchedulerState:
    def __init__(self):
        self.running = False  

scheduler_state = SchedulerState()

def click_button_return():
    simple_screen.window.destroy()
    panel_screen.panel_screen()

def monitor_f2_key():
    if keyboard.is_pressed('f2'):  # Verifica se a tecla F2 foi pressionada
        # Executa o invoke no contexto correto do tkinter
        simple_screen.window.after(0, simple_screen.buttons[0].invoke)  # Garante que o invoke seja executado no loop principal
        while keyboard.is_pressed('f2'):  # Aguarda a tecla ser liberada
            pass

    # Continua monitorando a tecla F2
    simple_screen.window.after(100, monitor_f2_key)

def click_button_start(window):
    if not scheduler_state.running:
        try:
            monitor_f2_key()
        except:
            pass
        simple_screen.buttons[0]._fg_color = 'yellow'
        simple_screen.buttons[0]._hover_color = 'yellow'
        simple_screen.buttons[0].configure(text_color='black')
        simple_screen.buttons[0].configure(text='PAUSAR')
        scheduler_state.running = True
        print('Sistema Iniciado')
        simple_screen.tk_async.start()
        tk_async.async_execute(
            func_exec_prod.func_exec_prod(scheduler_state), wait=False, visible=False, pop_up=False, callback=None, master=window
        )
    else:
        simple_screen.buttons[0]._fg_color = 'darkgreen'
        simple_screen.buttons[0]._hover_color = 'darkgreen'
        simple_screen.buttons[0].configure(text_color='white')
        simple_screen.buttons[0].configure(text='INICIAR')
        scheduler_state.running = False
        simple_screen.tk_async.stop()
        print('Sistema Pausado')



def exec_prodution():
    buttons_list = []

    buttons_list.append(simple_screen.ArrayButton('INICIAR', 'green', 'green4', lambda: click_button_start(simple_screen.window), 'Iniciar'))
    buttons_list.append(simple_screen.ArrayButton('VOLTAR',  'red', 'red4',  click_button_return, 'return'))

    simple_screen.create_screen('500x400', 'Exibir Lista', buttons_list)

if __name__ == '__main__':
    exec_prodution()