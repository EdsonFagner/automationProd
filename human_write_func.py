import keyboard
import time
from random import uniform

def human_write_func(word):
    for char in word:
        keyboard.write(char)
        time.sleep(uniform(0.05, 0.2))

if __name__ == "__main__":
    human_write_func()
