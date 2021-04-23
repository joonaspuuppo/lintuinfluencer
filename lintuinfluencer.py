#!/usr/bin/env python

from tweet import Tweet
from pynput import keyboard
import time
import csv
import gspread
from twython import Twython
import random

# Loop that creates Tweet-objects from user input, writes them to a file and tweets them

# Checks if all characters in a given string are the same.
def allCharactersSame(s):
    s1 = []
    for i in range(len(s)):
        s1.append(s[i])
    s1 = list(set(s1))
    if len(s1) == 1:
        return True
    else:
        return False

# Google API authorization
gc = gspread.service_account(filename='lintuinfluencer-5845e6883765.json')

# Open the Google sheet)
wks = gc.open("lintuinfluencer").sheet1

#Twitter API authorization
with open('twitteraccess.txt', 'r') as reader:
    API_KEY = reader.readline().split(": ", 1)[1].strip('\n')
    API_SECRET = reader.readline().split(": ", 1)[1].strip('\n')
    ACCESS_TOKEN = reader.readline().split(": ", 1)[1].strip('\n')
    ACCESS_TOKEN_SECRET = reader.readline().split(": ", 1)[1].strip('\n')

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

text = ""
previousText = ""
maxLength = 200

while (True):
    try:
        startTime = time.time()
        # Initialize text to an empty string
        text = ""
        # Randomize max tweet length
        maxLength = random.randint(30, 280)

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
            if len(text) == maxLength:
                return False
            if (len(text) > 10) and (time.time() - startTime > 180):
                return False
            
        # Collect events until released
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        # Create a new Tweet with text and time 
        newTweet = Tweet(text, time.strftime("%d.%m.%Y %H:%M:%S"))
        print(" " + newTweet.toString())
        
        # Append the tweet to a file
        with open('lintuinfluencer_data.txt', 'a', newline='') as csvfile:
            tweetwriter = csv.writer(csvfile, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            tweetwriter.writerow([newTweet.getText(), newTweet.getTime()])

        # Only post tweet if it's not too similar to the previous tweet.
        # Important in case a key gets stuck or whatever.
        if allCharactersSame(text) and allCharactersSame(previousText) and text[0] == previousText[0]:
            print("Duplicate tweet. Not tweeted.")
        else:
            # Append the tweet to a Google Sheet
            nextEmptyRow = wks.find("").row
            wks.update_cell(nextEmptyRow, 1, newTweet.getText())
            wks.update_cell(nextEmptyRow, 2, newTweet.getTime())

            # Post tweet
            twitter.update_status(status = newTweet.getText())
            print("Tweet!")

            # Mark tweet as tweeted
            wks.update_cell(nextEmptyRow, 3, "Y")

        previousText = text
    
    except Exception as e:
        with open("lintuinfluencer_errorlog.txt", "a") as myfile:
            myfile.write(repr(e) + "\n")
        print(repr(e))
