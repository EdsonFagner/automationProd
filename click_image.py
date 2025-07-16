import pyautogui
import time
def click_image(image):
    
    try:
        time.sleep(2)
        image_locate = pyautogui.locateCenterOnScreen(image)
        locate_x = image_locate.x
        locate_y = image_locate.y
        if image_locate is None:
            raise pyautogui.ImageNotFoundException(f'{image} não encontrada na tela.')
        else:
            pyautogui.click(locate_x, locate_y)
    except pyautogui.ImageNotFoundException as e:
        print(e)
        pass   