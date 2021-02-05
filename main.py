from tweet import Tweet
from pynput import keyboard
import time

# Loop that creates Tweet-objects from user input
# TODO: Save tweets to a file 

while (True):
    # Initialize text to an empty string
    text = ""

    # Listen to keyboard input
    def on_press(key):
        try:
            global text
            text += key.char
            print(key.char, end = '')
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

    # Create a new Tweet with text and time 
    newTweet = Tweet(text, time.strftime("%d.%m.%Y, %H:%M:%S"))
    print(" " + newTweet.toString())
    
    # Append the tweet to a file
    f = open("lintuinfluencer_data.txt", "a")
    f.write(newTweet.toString() + "\n")
    f.close()