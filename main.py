from tweet import Tweet
from pynput import keyboard
import time

text = ""

def on_press(key):
    try:
        global text
        text += key.char
    except AttributeError:
        text += ""
    # Stop listener
    if key == keyboard.Key.esc:
        return False
    if (len(text) == 280):
        return False
    
# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

newTweet = Tweet(text, time.strftime("%d.%m.%Y, %H:%M:%S"))
print(newTweet.toString())