import gspread

# Reads all tweets character by character and creates a text file
# that contains the overall frequency of each character in all tweets.
# Characters that don't appear at all aren't included in the file.

# Google API authorization
gc = gspread.service_account(filename='lintuinfluencer-5845e6883765.json')

# Open the Google sheet)
wks = gc.open("lintuinfluencer").sheet1

# Joining all tweets to a string
tweetList = wks.col_values(1)
tweetedList = wks.col_values(3)
tweetedTweetsList = []

i = 59
while i < 537:
    if tweetedList[i] == "Y":
        tweetedTweetsList.append(tweetList[i])
    i += 1

tweetsAsString = "".join(tweetedTweetsList)

#print(tweetsAsString)

# Creating a list where each index represents a characters ASCII value
charFreq = [0] * 255

# Going through tweetsAsString character by character.
# Each time a character appears, incrementing the corresponding charFreq list item value by one.
for i in range(len(tweetsAsString)):
    char = tweetsAsString[i]
    charValue = ord(char)
    charFreq[charValue] += 1

# Writing character frequency to a text file
with open("lintuinfluencer_charfreq.txt", 'w') as myFile:
    for i in range(len(charFreq)):
        if charFreq[i] != 0:
            #print(chr(i), " ", charFreq[i])
            row = chr(i) + " " + str(charFreq[i]) + "\n"
            myFile.write(row)
