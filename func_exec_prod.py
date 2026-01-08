import conection
import keyboard
import navigator_func
import asyncio
import login_func
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


async def func_exec_prod(scheduler_state):
    await asyncio.sleep(1)
    # Garantir que o navegador esteja inicializado
    if not hasattr(navigator_func, 'navegador'):
        navigator_func.navigator_settings()

    try:
        navigator_func.navegador.get('https://queimados.ecosistemas.com.br/Prime_Queimados/login.aspx')
        await asyncio.sleep(1)
        navigator_func.navegador.find_element(By.XPATH, '//*[@id="LoginView1_lgAcesso_UserName"]').click()
        await asyncio.sleep(1)
        #Digitar usuário
        navigator_func.navegador.find_element(By.XPATH, '//*[@id="LoginView1_lgAcesso_UserName"]').send_keys('14886471781')
        await asyncio.sleep(1)
        #Digitar senha
        navigator_func.navegador.find_element(By.XPATH, '//*[@id="LoginView1_lgAcesso_Password"]').send_keys('123')
        await asyncio.sleep(1)
        navigator_func.navegador.find_element(By.XPATH, '//*[@id="LoginView1_lgAcesso_Password"]').send_keys(Keys.ENTER)
        await asyncio.sleep(1)
        try:
                element = navigator_func.navegador.find_element(By.XPATH, '//*[@id="btnConfirmarLogin"]')
                if element:
                    element.click()
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"[func_exec_prod] Erro ao clicar no elemento: {e}")
            pass
    except Exception as e:
        print(f"[func_exec_prod] Erro ao acessar o navegador: {e}")
        return
        
    #Loop para pegar a lista de produção do banco de dados e executar as produções uma a uma
    sql_show_prod_list = f'SELECT * FROM prod_{login_func.nick_name}'
    conection.mycursor.execute(sql_show_prod_list)
    myresult_show_prod_list = conection.mycursor.fetchall()

    if myresult_show_prod_list:
        for i in range(0, len(myresult_show_prod_list)):
            navigator_func.navegador.find_element(By.XPATH, "//span[@class='rpText' and text()='Visita Domiciliar']").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//span[normalize-space(.) = 'Nova Visita Domiciliar e Territorial']").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[@type='radio' and @value='NOME']").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[@placeholder='Informe o nome do paciente']").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[@placeholder='Informe o nome do paciente']").send_keys(myresult_show_prod_list[i][1])
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[@placeholder='Informe o nome do paciente']").send_keys(Keys.ENTER)
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//a[img[contains(@src, 'right-arrow-laranja.png')]]").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[contains(@id, '_ClientState')]/preceding-sibling::input[contains(@class, 'riTextBox')]").click()
            await asyncio.sleep(1)
            navigator_func.navegador.find_element(By.XPATH, "//input[contains(@id, '_ClientState')]/preceding-sibling::input[contains(@class, 'riTextBox')]").send_keys(myresult_show_prod_list[i][2])
            await asyncio.sleep(1)
            
            #Loop para selecionar os checkbox
            for x in range(1, myresult_show_prod_list[i][3]+1):
                navigator_func.navegador.find_element(By.XPATH, f"(//input[contains(@id, 'chkPresentenaVisita')])[{x}]").click()
                await asyncio.sleep(1)
            #Loop para selecionar os arrows
            for y in range(1, myresult_show_prod_list[i][3]+1):    
                navigator_func.navegador.find_element(By.XPATH, f"(//td[input[@title='Visita Domiciliar']])[{y}]").click()
                await asyncio.sleep(1)
                navigator_func.navegador.find_element(By.XPATH, "//input[contains(@id, 'chkMotivoConsulta')]").click()
                await asyncio.sleep(1)
                navigator_func.navegador.find_element(By.XPATH, "//input[@type='checkbox' and contains(@id, 'chkMotivoConsulta_1')]").click()
                await asyncio.sleep(1)
                navigator_func.navegador.find_element(By.XPATH, "//input[@type='checkbox' and contains(@id, 'chkMotivoOutros_3')]").click()
                await asyncio.sleep(1)
                navigator_func.navegador.find_element(By.XPATH, "//span[contains(@id, 'rbSalvarPaciente')]").click()
                await asyncio.sleep(1)

            try:
                navigator_func.navegador.find_element(By.XPATH, "//span[contains(@id, 'rbSalvar')]").click()
                
            except Exception as e:
                print(f"[func_exec_prod] Erro ao clicar no elemento: {e}")
                pass
            await asyncio.sleep(1)
            try:
                WebDriverWait(navigator_func.navegador, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'rwDialog') and contains(., 'Visita domiciliar salva com sucesso.')]//a[.//span[normalize-space()='OK']]"))
                )
            except Exception as e:
                print(f"[func_exec_prod] Erro ao clicar no elemento: {e}")
                pass
            await asyncio.sleep(1)
            try:
                navigator_func.navegador.find_element(By.XPATH, "//span[contains(@class, 'RadButton') and normalize-space(.) = 'Fechar']").click()
            except Exception as e:
                print(f"[func_exec_prod] Erro ao clicar no elemento: {e}")
                pass
            await asyncio.sleep(1)
            print('Chegou ate aqui')





if __name__ == '__main__':
    func_exec_prod()