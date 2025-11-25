from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
    

def navigator_settings():
    global navegador
    servico = Service(ChromeDriverManager().install())
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("--log-level=3")
    option.add_argument("--memory-limit=4G") 
    navegador = webdriver.Chrome(service=servico, options=option)
    navegador.maximize_window()
    time.sleep(1)
    navegador.get('https://queimados.ecosistemas.com.br/Prime_Queimados/login.aspx')

if __name__ == '__main__':
    navigator_settings()