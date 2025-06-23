#encoding: utf-8
import os
import login_func
import time

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def main ():
    login_func.login()
    time.sleep(1)
    if(login_func.success_login == True):
        print('Acesso Autorizado')
    else:
        print('Acesso Negado')    

if __name__ == '__main__':
    main()
